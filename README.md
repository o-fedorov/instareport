# instareport

Report propaganda accounts on Instagram
Оскаржуємо пропагандистські аккаунти Інстаграму

## ENG

The script uses Instagram credentials to report the accounts.
Since it may violate the Instagram terms and conditions, and requires
multifactor authentication to be disabled,
it is better to register a dedicated Instagram account and
use its credentials.

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
poetry run instareport channels.txt
```

## UKR

Скрипт використовує логін та пароль облікового запису Інстаграму,
щоб скаржитись на аккаунти.  Для використання скрипта рекомендуємо зареєструвати
окремий обліковий запис, оскільки скрипт потенційно може порушувати
правила Інстаграму, а також тому що для нормальної роботи скрипта
багатофакторна аутентифікація має бути відключена (
сподіваюся, ви підключили багатофакторну аутентифікацію для свого особистого
аккаунта, і це не коди через СМС).

### Використання

Вам потрібно мати [Python](https://www.python.org/downloads/) версії
щонайменше 3.8, та [poetry](https://python-poetry.org/docs/#installation).

Клонуйте репозиторій.  Відкрийте термінал / консоль командного рядка,
перейдіть до директорії репозиторію, і встановіть залежності.

```shell
poetry install --no-dev
```

Іх терба встановити лише раз.

Підготуйте текстовий файл із іменами акаунтів, на які бажаєте поскаржитись,
по одному аккаунту на рядок, як наведено нижче:

```text
secured_borders_
rainbow_nation_us
_blacktivistt_
```

Збережіть аккаунти у файл, наприклад `accounts.txt`.
Запустіть команду, як на прикладі нижче.  За запитом, введіть
ім'я користувача та пароль.  Зауважте, що символи паролю не відображаються
коли ви їх набираєте.

```shell
poetry run instareport channels.txt
```
