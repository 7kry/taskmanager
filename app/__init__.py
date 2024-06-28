from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config, translations
from app.utils import get_translation

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'
migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  login.init_app(app)
  migrate.init_app(app, db)

  @app.context_processor
  def inject_helpers():
    return dict(translations=translations, get_translation=get_translation)

  with app.app_context():
    from . import routes, models
    from .forms import TaskForm, TaskTypeForm, CompanyForm

    db.create_all()

  return app

# vim:ft=2:ts=2:sts=2:sw=2:et
