import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get(",6641518289:AAE1wJqQy4jE-hFPRMowpZDjy3QtdVgfHFA "")
 

    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("22047737", 12345))


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("1BVtsOIgBu7xLh7BgmuKp5OXoWtnQ2796yF9pr9MQQ54xRcXMsSJk_YjECJ8Vp2u2Wh0n7MYuFHjYbZDw5-NlPFatcW3p8t0nrnDUpikPXm4AGHP5dLaIMiOnRhlP1l6bFWQpzYo-m8Gk8xfPFH6R4EJiK9UzQHoHdvnm1Nf1t59chNiCXMcosr5cuZ-CmLgo_McA5OSIIeuSxq29bXsMc2d2zmFI5j7J3uLeH2KWcVbhPmJT_j1JmFItN7GXXLNCNFC9IXasgJGI41wnsEVfg7r9yR9YB7yPU_tXfq3aUg0dM1vyUF71MLQcDnfhGDWqYEpk5QVUuGxiAdfctcOxaBwlmBjogGM=", "")
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("DATABASE_URI", "")


    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))


    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


    # To record start time of bot
    BOT_START_TIME = time.time()
