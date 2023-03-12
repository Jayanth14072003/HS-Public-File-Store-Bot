import os

API_ID = int(os.environ.get("API_ID", '10261086'))
API_HASH = os.environ.get("API_HASH", '9195dc0591fbdb22b5711bcd1f437dab')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '5847069255:AAEKV-j7aNWIwmwl8wavyxiIqjbP7C3hVyg')
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", '-1001624276333')
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID",'1426588906'))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'Hs_Botz')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
