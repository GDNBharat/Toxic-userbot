import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27639080")) #optional
API_HASH = getenv("API_HASH", "5c10faa5b68227793d5f9084106c6f24") #optional

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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGlvSgAgbdEafeMy9YsHcLA0jMFmQ_yJIEBERIX83clQNauiZcVyAFb0Ga232bVbacVjNehemr44i5pTMJaaDp2hGkhULI5kko0lKN0l8aYthjp4bS2zvHCxJ48DLNH3il0nlb-GINXzwgV8Kqz8RVc1WNsLrxZfSRWs3KUTNX4rnWFIcpD1VuW701fXi-GN9rXAuMWTiHkhCwzJIioxS5p-GSOpigZvaXJsAwZCyjidTzvS1mdvYq6zqQqXgfWLkzEf_8st5KBNWYWVnm2gc5KcqqyQmxaCFb-4_n276FONQpyGv7JhyBWgQgcKh6CJiaQKsvHcHr3TcpdZaNJ-0CTQQVFUAAAAAHflqnaAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
