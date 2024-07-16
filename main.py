import os

from flask import Flask

from init import db, ma, bcrypt, jwt

def initialise_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth
    app.register_blueprint(auth)

    from controllers.grocery_list_controller import grocery_list
    app.register_blueprint(grocery_list)

    return app