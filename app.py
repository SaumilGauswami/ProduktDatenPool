from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from views import *

if __name__ == '__main__':
    app.run(debug=True)
