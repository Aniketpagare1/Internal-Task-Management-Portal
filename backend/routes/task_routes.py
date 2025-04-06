from flask import Blueprint, request, jsonify
from models import db, Task, User
from functools import wraps
import jwt
from config import Config
from utils.email_sender import send_task_email
from datetime import datetime

task_bp = Blueprint('tasks', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace("Bearer ", "")
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            user = User.query.get(data['user_id'])
            if not user:
                raise Exception()
        except:
            return jsonify({'message': 'Token is invalid or expired'}), 401
        return f(user, *args, **kwargs)
    return decorated

@task_bp.route('/api/tasks', methods=['POST'])
@token_required
def assign_task(current_user):
    if current_user.role != 'manager':
        return jsonify({'message': 'Not authorized'}), 403

    data = request.json
    task = Task(
        title=data['title'],
        description=data['description'],
        deadline=datetime.strptime(data['deadline'], '%Y-%m-%d'),
        assigned_to=data['assigned_to']
    )
    db.session.add(task)
    db.session.commit()

    assigned_user = User.query.get(data['assigned_to'])
    send_task_email(assigned_user.email, task.title, task.deadline)

    return jsonify({'message': 'Task assigned'}), 201

@task_bp.route('/api/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = Task.query.filter_by(assigned_to=current_user.id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'deadline': t.deadline.strftime('%Y-%m-%d'),
        'status': t.status
    } for t in tasks])

@task_bp.route('/api/tasks/<int:task_id>/status', methods=['PUT'])
@token_required
def update_status(current_user, task_id):
    task = Task.query.get(task_id)
    if task.assigned_to != current_user.id:
        return jsonify({'message': 'Not allowed'}), 403

    task.status = request.json['status']
    db.session.commit()
    return jsonify({'message': 'Status updated'})
