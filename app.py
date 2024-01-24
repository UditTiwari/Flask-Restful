from flask import Flask
from api.views import blueprint
from dotenv import load_dotenv
from extensions import db
import os
load_dotenv()


app = Flask(__name__)

app.register_blueprint(blueprint=blueprint)
app.config.from_object("config")


db.init_app(app)


if __name__=='__main__':
    # app.run(host=host,port=port,debug=debug)

    app.run(host=app.config.get("host"),port=8000,debug=app.config.get("debug"))