import os
from dotenv import load_dotenv
load_dotenv()


debug = os.environ.get("FLASK_DEBUG")
host = os.environ.get("FLASK_HOST","0.0.0.0")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
