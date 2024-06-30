from app import db

class TaskType(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=True, unique=True)

# vim:ts=2:sts=2:sw=2:et
