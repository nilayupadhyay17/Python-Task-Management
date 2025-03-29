from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Task, db

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    new_task = Task(title=data["title"], user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Task created"}), 201

@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks])
