from datetime import datetime
from app import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    activity_type = db.Column(db.String(64))
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Activity {self.activity_type} for Task {self.task_id} by User {self.user_id}>'

# vim:ts=2:sts=2:sw=2:et
