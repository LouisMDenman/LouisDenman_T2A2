import os

from flask import Flask
from marshmallow.exceptions import ValidationError

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

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth
    app.register_blueprint(auth)

    from controllers.grocery_list_controller import grocery_list
    app.register_blueprint(grocery_list)

    from controllers.connection_controller import connections
    app.register_blueprint(connections)

    from controllers.product_controller import product
    app.register_blueprint(product)

    from controllers.product_list_controller import product_list
    app.register_blueprint(product_list)

    return app