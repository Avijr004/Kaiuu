
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 23653093 # integer value, dont use ""
    API_HASH = "ee6df88753c36eeab95391940ba3844f"
    TOKEN = "6491531689:AAFaxNvZyiyPE8lhZlo2dNv45yZoHVjSSIQ"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1556830659 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "its_witch_here"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png"
    EVENT_LOGS = (-1001603027566)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "MONGO_DB_URI", "mongodb+srv://karjr002:INCyT5eXfqjoiYQ4@cluster0.6swcped.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://joestroq:xFuhuUu_XRrZA-KzUkCNLWVq14qT4yIu@isabelle.db.elephantsql.com/joestroq"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "D5UJD8IQE34NXJ0O"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "F8NYGXSAEEC4"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
