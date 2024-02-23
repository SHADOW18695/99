import os
from os import getenv

API_ID = getenv("API_ID", "25703106")

API_HASH = getenv("API_HASH", "75cb4ce927cd3da265bbf86942c371f9")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6896439329:AAFSJV97z7zzot3wmJUVi7uwLO9p2UW7lSU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

sudo_group = -1003684833654
sudo_user = 5685478868
log_channel = -1005643367899

# try:
#     ADMINS=[]
#     for x in (os.environ.get("ADMINS", "5760012562 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
#         ADMINS.append(int(x))
# except ValueError:
#         raise Exception("Your Admins list does not contain valid integers.")
# ADMINS.append(OWNER)


