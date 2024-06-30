from datetime import datetime
from app import db

task_company = db.Table('task_company',
  db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
  db.Column('company_id', db.Integer, db.ForeignKey('company.id'))
)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  task_type_id = db.Column(db.Integer, db.ForeignKey('task_type.id'))
  task_detail = db.Column(db.String(256))
  required_time = db.Column(db.Integer)
  ordered_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  order_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  message = db.Column(db.Text)
  is_completed = db.Column(db.Boolean, default=False)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  task_type = db.relationship('TaskType', backref='tasks')
  companies = db.relationship('Company', secondary=task_company, backref=db.backref('tasks', lazy=True))

# vim:ts=2:sts=2:sw=2:et
