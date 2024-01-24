from flask import Flask
from api.views import blueprint
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)

app.register_blueprint(blueprint=blueprint)


debug = os.environ.get("FLASK_DEBUG")
host = os.environ.get("FLASK_HOST","0.0.0.0")
port = os.environ.get("FLASK_PORT",8000)

if __name__=='__main__':
    app.run(host=host,port=port,debug=debug)