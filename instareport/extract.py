"""Extract instagram accounts from a list of links."""
import re
import click


@click.command()
@click.argument("output_file", type=click.File("w"))
def main(output_file):
    """Extract Instagram accounts from a text."""
    print("Enter the text with Instagram links, press Ctr+C when done.")

    accounts = set()

    try:
        while True:
            line = input()
            accounts.update(s for s in re.findall(r"instagram\.com/([^/?]{3,})", line))
    except KeyboardInterrupt:
        for account in accounts:
            print(account, file=output_file)
        print("Done")


if __name__ == '__main__':
    main()
