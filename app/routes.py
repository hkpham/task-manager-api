from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from . import db
from .models import Task

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        status=data.get("status", "pending")
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@main.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@main.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

@main.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify(task.to_dict())

@main.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200
