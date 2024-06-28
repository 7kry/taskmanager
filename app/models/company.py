from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    tasks = db.relationship('Task', secondary='task_company', backref=db.backref('companies', lazy='dynamic'))

# vim:ts=2:sts=2:sw=2:et
