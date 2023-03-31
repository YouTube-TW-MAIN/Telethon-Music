import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "15077074"))
    API_HASH = os.environ.get("API_HASH", "5707eaedbdd57f22e7b7cddd5ad7db6e)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6151505647:AAGLewcnDAFd537Fc5VbLet1X41g0eGSyzQ)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLgBuzeHbX-05l26kWv9l7lLLvib9bZRBqtr7RPJPaNtoZxjC25MqZTttUCHmbKMU4PGZu4Y_0AAXGkwuXTGfAo6KJut3wFEYBqg0abNZ0AhlqFWUlIcd-BFk3nCX4W3fD6jyTqhkKbeUxqZAFYcZWoG_SMLfmc0QvKRc8LOGPrsGDwoOV7IHt0P8gS7PdNgl794plPzKZHNTSbJw8pse8BQ6xMjt7QEB4bx-o4b0tqIc8mg0_-Nt2ooMzxFqzbDkwQgV0QMA1R4hhpvnN90EZn7Tzl9j5wb4pRIwxCUILKHQIM2WSaXglqIXmk5FG67VdYzOuemLzoIje-hn8gYGBZrUdQ=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9e5d9f45b21d80bc15444.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9e5d9f45b21d80bc15444.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
