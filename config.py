import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28362850")) #optional
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8187405882").split()))
OWNER_ID = int(getenv("OWNER_ID", "8187405882"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7500951257:AAFwz8XYQ_bFBjiqcFeE9yN0QfU3-Kl6gik")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/6d78e1e8de6339de61236-35d9fdfe123743c20f.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1002532559194")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GDNBharat/Toxic-userbot")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwyGIAvBcKzAYNr0ZDR2WqgfvXDL8Gop3R7GpDlPwwdVrayaawBfwg4OIAmIErMuhKDCYsS7xWF3Xf4UyCzyfqLh7HHxpWeD3UQO6dQ4v-EwioCJKrNLvB0UALXDC-ZPviw0jHfopyEbBe5QXFTdHd6Ppyo6kmna6Y6LKa5ts0vJaJ2GudwEk_qdhPFczvsvGv4HtXpCet1_pmHfccWH-PHo9hQXsd9Kug7QTF3kaMpVXWjA9pSEv5ofqK0uguIgvMbgrfENX5GjH8Q_avCsAwsYr_5QrMlHMHM1Vw0NoY12BX_G1GW3Z11mPPZMQUC6ZVCZZDYI5m79egeLjak2_Eqg84HAAAAAHoAeY6AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
