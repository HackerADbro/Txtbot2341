import os

API_ID = API_ID = 25567551

API_HASH = os.environ.get("API_HASH", "45993062e6b160a7a360d648ecc8e43a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6629981026:AAGqnnK7GGTl-zBZKg3TdkgucrzPPM158nU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1318247204))

LOG = -4023753212

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6034357260").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
