#Standard library imports
import os

#Third party imports
from flask import Flask
from marshmallow.exceptions import ValidationError

#Local application imports
from init import db, ma, bcrypt, jwt

#Function that is responsible for initialising the app.
def initialise_app():
    app = Flask(__name__)

    #Configure the app to display JSON output as it is listed instead of sorting it for better result formatting.
    app.json.sort_keys = False

    #Retrieve the relevant database details from the .env file.
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    #Retrieve the relevant JWT key from the .env file.
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    #Take the initialised libraries from init and initialise them within the app.
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    #Error handling route that displays the relevant error encounted within the app.
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    #import and register the controller blueprints for the app.
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth
    app.register_blueprint(auth)

    from controllers.grocery_list_controller import grocery_list
    app.register_blueprint(grocery_list)

    from controllers.comment_controller import comments
    app.register_blueprint(comments)

    from controllers.connection_controller import connections
    app.register_blueprint(connections)

    from controllers.product_controller import product
    app.register_blueprint(product)

    from controllers.product_list_controller import product_list
    app.register_blueprint(product_list)

    #Once all is initialised, return the app.
    return app