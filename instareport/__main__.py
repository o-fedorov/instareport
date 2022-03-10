import os
import time
from json import JSONDecodeError

import click
import requests


@click.command()
@click.option("--username", prompt=True, default=lambda: os.environ.get("USER", ""))
@click.password_option(confirmation_prompt=False)
@click.option("-w", "--wait", default=3.0, type=float, help="wait time between calls.")
@click.option("--check", is_flag=True, help="Just check if the account is alive, without any report.")
@click.argument("input_file", type=click.File("r"))
def report(input_file, username, password, wait, check):
    session = requests.session()
    accounts_stats = {}

    login_resp = session.post(
        "https://www.instagram.com/accounts/login/ajax/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.8,uk-UA;q=0.5,uk;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "X-CSRFToken": "l63IoyUQDFEjGPGkrdZISRYc4UeyB1Mt",
            "X-Instagram-AJAX": "bc16efce305d-hot",
            "X-IG-App-ID": "936619743392459",
            "X-ASBD-ID": "198387",
            "X-IG-WWW-Claim": "0",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.instagram.com",
            "DNT": "1",
            "Referer": "https://www.instagram.com/",
            "Cookie": "csrftoken=l63IoyUQDFEjGPGkrdZISRYc4UeyB1Mt; mid=YinRkwAEAAEXlCQkpHtQXyvHlL3g; ig_did=FE79328A-DA5E-41E0-9AC7-7E1D4A506896; ig_nrcb=1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        },
        data={
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
            "queryParams": "{}",
            "optIntoOneTap": "false",
        },
    )

    if 'authenticated":true' in login_resp.text or "userId" in login_resp.text:
        session.headers.update({"X-CSRFToken": login_resp.cookies["csrftoken"]})
    else:
        print("\n\nLogin failed:\n", login_resp.text, "\n\n")
        return

    for target_account in input_file:
        target_account = target_account.strip()

        print(f"Reporting of {target_account}")

        account_details_resp = session.get(
            f"https://www.instagram.com/{target_account}/?__a=1"
        )

        try:
            account_id_payload = account_details_resp.json()
        except JSONDecodeError:
            print(
                "\n\nFailed to get account ID:\n",
                account_details_resp.status_code,
                account_details_resp.text,
                "\n\n",
            )
            continue

        try:
            account_id = account_id_payload["graphql"]["user"]["id"]
        except KeyError:
            if account_id_payload:
                print(
                    "\n\nFailed to get account ID:\n",
                    account_details_resp.status_code,
                    account_id_payload,
                    "\n\n",
                )
            else:
                print("The account is already off")
                accounts_stats[False] = target_account
            continue

        accounts_stats[False] = target_account

        if check:
            continue

        report = session.post(
            f"https://www.instagram.com/users/{account_id}/report/",
            data={"source_name": "", "reason_id": "5", "frx_context": ""},
        )

        if '"status":"ok"' in report.text:
            print("Successfully reported.")
        else:
            print("\n\nError:\n", report.text, "\n\n")

    time.sleep(wait)

    print("Done. Already disabled accounts:", len(accounts_stats[False]), "still active:", len(accounts_stats[True]))
    print("Active accounts:")
    for account in accounts_stats[True]:
        print(account)


if __name__ == "__main__":
    report()
