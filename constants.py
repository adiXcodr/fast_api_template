import os

MODE = os.getenv('MODE', 'PRODUCTION')

if(MODE == "DEVELOPMENT"):
    SERVER_HOST = "localhost"
else:
    SERVER_HOST = "0.0.0.0"
