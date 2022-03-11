# instareport

Report propaganda accounts on Instagram
Оскаржуємо пропагандистські аккаунти Інстаграму

## ENG

The script uses Instagram credentials to report the accounts.
Since it may violate the Instagram terms and conditions, and requires
multifactor authentication to be disabled,
it is better to register a dedicated Instagram account and
use its credentials.

Note that Instagram can limit the number of actions you can perform at
a time.  The script already has a timeout of 3 seconds between calls,
though if you run the script multiple times, therefore signing in
multiple times for a short period of time, Instagram can temporary block
your ability to sign in.

Also, note that some of accounts you are reporting may be inaccessible
for your location, in this case it is better to use VPN that changes
your IP location, or run the script from a server that is located in
another country.

### Usage

Ensure you have [Python](https://www.python.org/downloads/) of at
least version 3.8, and
[poetry](https://python-poetry.org/docs/#installation) installed.

Clone the repository.  Open a terminal, navigate to the directory
of the repo and install the dependencies.

```shell
poetry install --no-dev
```

You need to install them only once.

Prepare a text file with accounts, one account per line, like following:

```text
secured_borders_
rainbow_nation_us
_blacktivistt_
```

Store the accounts in a file like `accounts.txt`.

Then run the command like the one below.  You will be prompted for your
Instagram username and password.  Note that
the password is not displayed when you type it in.

```shell
poetry run instareport accounts.txt
```

There is also a tool to extract accounts from arbitrary text containing
Instagram links, call it as `poetry run instareport accounts.txt` and
follow the instructions.

## UKR

Скрипт використовує логін та пароль облікового запису Інстаграму,
щоб скаржитись на акаунти.  Для використання скрипта рекомендуємо зареєструвати
окремий обліковий запис, оскільки скрипт потенційно може порушувати
правила Інстаграму, а також тому що для нормальної роботи скрипта
багатофакторна аутентифікація має бути вимкнена (
сподіваюся, ви додали багатофакторну аутентифікацію для свого особистого
акаунта, і це не коди через СМС).

Завважте, що Інстаграм може обмежувати кількість дій, що ви виконуєте
за певний час.  Щоб цього уникнути, скрипт чекає 3 секунди між запитами,
проте якщо ви запускаєте скрипт кілька разів підряд, і таким чином
авторизуєтесь кілька разів за короткий проміжок часу, Інстаграм може
тимчасово заблокувати вам можливість входити в обліковий запис.

Також, зверніть увагу що облікові записи, на які ви скаржитесь,
можуть бути недоступні для того місця, де ви розташовані.  В цьому
випадку краще використовувати VPN що змінює ваше місце за IP адресою,
або можна запустити скрипт із сервера що розміщений в іншій країні.

### Використання

Вам потрібно мати [Python](https://www.python.org/downloads/) версії
щонайменше 3.8, та [poetry](https://python-poetry.org/docs/#installation).

Клонуйте репозиторій.  Відкрийте термінал / консоль командного рядка,
перейдіть до директорії репозиторію, і встановіть залежності.

```shell
poetry install --no-dev
```

Іх треба встановити лише раз.

Підготуйте текстовий файл із іменами акаунтів, на які бажаєте поскаржитись,
по одному акаунту на рядок, як наведено нижче:

```text
secured_borders_
rainbow_nation_us
_blacktivistt_
```

Збережіть акаунти у файл, наприклад `accounts.txt`.
Запустіть команду, як на прикладі нижче.  За запитом, введіть
ім'я користувача та пароль.  Зауважте, що символи паролю не відображаються
коли ви їх набираєте.

```shell
poetry run instareport accounts.txt
```

Також є програма, що знаходить назви аканутів в будь-якому тексті
що містить Instagram-посилання, запустіть її так:
`poetry run instareport accounts.txt` , вставте текст в термінал,
і в кінці натисніть комбінацію клавіш `Ctr+C` (`Cmd+C`).
