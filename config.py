import os

class Config(object):
     # get a token from @BotFather
     TOKEN = os.environ.get("TOKEN", "")
     # The Telegram API things
     APP_ID = int(os.environ.get("APP_ID", "22947812"))
     API_HASH = os.environ.get("API_HASH", "dc45dab9ea0e2855846f6bc69cf74012")
     #Array to store users who are authorized to use the bot
     ADMIN = os.environ.get("ADMIN", "5080889208")
     #Your Mongo DB Database Name
     DB_NAME = os.environ.get("DB_NAME", "dsbro")
     #Your Mongo DB URL Obtained From mongodb.com
     DB_URL = os.environ.get("DB_URL", "mongodb+srv://dsbro:dsbro@cluster0.gtu48kz.mongodb.net/?retryWrites=true&w=majority")
