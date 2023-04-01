import os

API_ID = int(os.environ.get("API_ID", '3393749'))
API_HASH = os.environ.get("API_HASH", 'a15a5954a1db54952eebd08ea6c68b71')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '1892142872:AAFIkvJRdHmx_l3SAqr_Ol8AkIG_5EABgsE')
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", '-1001981909884')
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID",'1061576483'))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "0").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
