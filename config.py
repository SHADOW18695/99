import os
from os import getenv

API_ID = getenv("API_ID", "16478649")

API_HASH = getenv("API_HASH", "78dgjgsdgbsihgdia444yb85d9427894796c5c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5844832724:AAGoKwY_Hnjtrgewjnalwixijy_7tHfBDA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

sudo_group = -10021406843333
sudo_user = 550468565
log_channel = -100193547696574

# try:
#     ADMINS=[]
#     for x in (os.environ.get("ADMINS", "5760012562 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
#         ADMINS.append(int(x))
# except ValueError:
#         raise Exception("Your Admins list does not contain valid integers.")
# ADMINS.append(OWNER)


