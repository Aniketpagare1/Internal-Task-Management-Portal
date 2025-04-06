from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20))  # 'manager' or 'employee'
    password = db.Column(db.String(255))

    tasks = db.relationship("Task", backref="assigned_user", lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    status = db.Column(db.String(20), default="pending")
    assigned_to = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
