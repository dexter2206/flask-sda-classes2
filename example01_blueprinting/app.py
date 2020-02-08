from flask import Flask
from example01_blueprinting.views.hello_world import hello
from example01_blueprinting.views.users import users
from example01_blueprinting.views.posts import posts

app = Flask(__name__)
app.register_blueprint(hello, url_prefix="/hello")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(posts, url_prefix="/posts/<int:uid>/")


if __name__ == "__main__":
    app.run()
