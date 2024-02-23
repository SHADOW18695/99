import os
from os import getenv

API_ID = getenv("API_ID", "15964059")

API_HASH = getenv("API_HASH", "786fd04eca38875885d9427894796c5c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6600283424:AAGoKwY_HnjtzdTydpOCtgnNCjy_7tHfBDA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

sudo_group = -1002140793226
sudo_user = 5504336689
log_channel = -1001908668665

# try:
#     ADMINS=[]
#     for x in (os.environ.get("ADMINS", "5760012562 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
#         ADMINS.append(int(x))
# except ValueError:
#         raise Exception("Your Admins list does not contain valid integers.")
# ADMINS.append(OWNER)


