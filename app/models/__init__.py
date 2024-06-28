from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'

from .user import User
from .task import TaskType, Company, Task

# vim:ft=2:ts=2:sts=2:sw=2:et
