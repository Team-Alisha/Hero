from os import getenv
import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists("Internal"):
    load_dotenv("Internal")

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5207167635:AAEXpSbNBezE2SE8-leUlPFO3VHzchU_dWU")
API_ID = int(getenv("API_ID", "10597052"))
API_HASH = getenv("API_HASH", "2fd331fde4a6359a9cf0422cfbb4c900")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AsadAli:AsadAli@cluster0.3ejv7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5441658106").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5441658106").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001631416406"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Alisha Music")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Team-Alisha/Hero"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL", "Sad_shayari_lovers")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP", "Alisha_Support")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1", "BQCQAVYP1gZENAzQEBg1mnXT-lmjl3wN5e9mIRAqBcXvAGdZeV4MS8YB6PL8okxAjynGUkxQ4KsApGqX3jInax_HRHcXl5N2opbhxxuvZwINIMPcJaAQpNGTGT0y9W912P7lRmlA585k3SqiWR0OrrA97LAszSXrvx9dLyT5Bzv5Z-I1UO-9G6ffIZLWAREIXiYgahfBU0AGmpBJGQ--rhltM8DfL-pBk9wwIBmO7RfTa1n1zhQqauMfrYun_9yTvR-3lbEqmMTZFedBSKDXv5IsCb8loq_UYPTFF5ckd8Gn56Kn1j6jEuWS-pHiphfo7wF0lcc86tYx7rcxEpuh_KMxAAAAAWHrRD8A")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
