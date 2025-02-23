import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20857679"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a42de9e9451e7d01997f216bf6b3f647")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "834465886"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://techykr:Prwq3RZfYhMofFDK@cluster0.e2nfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "skforwardbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
