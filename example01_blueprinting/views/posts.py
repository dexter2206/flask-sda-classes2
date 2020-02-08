from flask import Blueprint, jsonify

posts = Blueprint("posts", __name__)


POSTS = {
    1: [
        {"title": "My first post", "body": "First post of kjalowiecki!"},
        {"title": "My second post", "body": "This is my second post "},
    ],
    2: [{"title": "Building blueprinted Flask apps", "body": "This is how you use Blueprints..."}],
}


@posts.route("/")
def user_posts(uid):
    if uid in POSTS:
        return jsonify({"posts": POSTS[uid]})
    else:
        return jsonify({"error": "Not found"}), 404


@posts.route("/<int:post_num>")
def user_post(uid, post_num):
    if uid in POSTS and len(POSTS[uid]) > post_num:
        return jsonify(POSTS[uid][post_num])
    else:
        return jsonify({"error": "Not found"}), 404
