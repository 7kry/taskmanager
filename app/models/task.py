from app import db
from datetime import datetime

task_companies = db.Table('task_companies',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'), primary_key=True)
)

class TaskType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return f'<TaskType {self.name}>'

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return f'<Company {self.name}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_type_id = db.Column(db.Integer, db.ForeignKey('task_type.id'), nullable=False)
    task_type = db.relationship('TaskType', backref=db.backref('tasks', lazy=True))
    companies = db.relationship('Company', secondary=task_companies, lazy='subquery',
        backref=db.backref('tasks', lazy=True))
    required_time = db.Column(db.Integer, nullable=False)
    ordered_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ordered_by = db.relationship('User', foreign_keys=[ordered_by_id])
    delegated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    delegated_by = db.relationship('User', foreign_keys=[delegated_by_id])
    order_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_to = db.relationship('User', foreign_keys=[order_to_id])
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'
        
# vim:ft=2:ts=2:sts=2:sw=2:et
