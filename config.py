#!/usr/bin/env python3


### Importing
from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("BOT_TOKEN", "7087741098:AAFhQ6yKXdScmNcKPlutvHL1sHhUKdb5dws") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(environ.get("API_ID", 22672907)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", 6287591671)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://infotechhero890:7c2qvHdJUYqTOaMa@cluster0.veojhex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    
