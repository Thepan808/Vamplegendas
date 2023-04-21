import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 4954361
    API_HASH = "43a786a8548a30f9d6887e36d53c0e64"
    BOT_TOKEN = "5111552136:AAH-1j9xSn6XvxzPm7DHM1_6nchfXW9r7tE"
    DATABASE_URL = "postgres://sjbigejk:5DexFs6Is0tRBMApihfGUfrrTQdSLraE@motty.db.elephantsql.com/sjbigejk"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "botslogsofc"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
