"""Blueprint for users-related views."""
from flask import Blueprint, jsonify

USERS = [
    {"id": 1, "username": "kjalowiecki", "email": "dexter2206@gmail.com"},
    {"id": 21, "username": "anowak", "email": "anowak@example.com"}
]

users = Blueprint("users", __name__)


@users.route("/<int:uid>")
def get_user(uid: int):
    for user in USERS:
        if uid == user["id"]:
            return jsonify(user)
    return jsonify({"error": "Not found"}), 404
