from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
import flask_monitoringdashboard as dashboard

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_secret_key')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site.db')
app.config["TESTING"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'
bcrypt = Bcrypt(app)
csp_policy = {
    'default-src': ["'self' https://ajax.googleapis.com https://cdnjs.cloudflare.com https://unpkg.com https://pypi.org"],
    'img-src': ["'self'", 'data:'],
    'script-src': ["'self' 'unsafe-eval' https://ajax.googleapis.com https://cdnjs.cloudflare.com https://unpkg.com https://pypi.org"],
    'style-src': ["'self' 'unsafe-inline'"]
}
Talisman(app, content_security_policy=csp_policy, frame_options='DENY', force_https=False)

from todo_project import routes
csrf = CSRFProtect(dashboard.bind(app))