from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  language = db.Column(db.String(2), default='en')

  tasks_ordered = db.relationship('Task', foreign_keys='Task.ordered_by_id', backref='ordered_by', lazy='dynamic')
  tasks_received = db.relationship('Task', foreign_keys='Task.order_to_id', backref='order_to', lazy='dynamic')

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

# vim:ts=2:sts=2:sw=2:et
