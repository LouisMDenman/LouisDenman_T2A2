#Standard library imports
from datetime import timedelta

#Third party imports
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

#Local application imports
from models.user import User, user_schema, UserSchema
from init import bcrypt, db

#Create an Authorisation Blueprint for the app.
auth = Blueprint("auth", __name__, url_prefix="/auth")

#Route that handles registering a user.
@auth.route("/register", methods=["POST"])
def register_user():
    try:
        #Retrieve JSON data.
        body_data = UserSchema().load(request.get_json())

        #Create a new user with provided JSON data.
        user = User(
            first_name = body_data.get("first_name"),
            last_name = body_data.get("last_name"),
            display_name = body_data.get("display_name") or f"{body_data.get("first_name")}{body_data.get("last_name")}",
            email = body_data.get("email")
        )

        password = body_data.get("password")
        #Hash password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        #Add user to a transaction and commit row to the database.
        db.session.add(user)
        db.session.commit()

        #Return the new user.
        return user_schema.dump(user), 201
    #Otherwise raise a relevant error and acompanying message.
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "That email is already in use, please try another email."}, 409
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404

#Route responsible for logging a user in.
@auth.route("/login", methods=["POST"])
def user_login():
    try:
        #Retrieve JSON data.
        body_data = request.get_json()
        #Create a statement that will find user based on their email.
        stmt = db.Select(User).filter_by(email=body_data.get("email"))
        #Retrieve this row from the database and store it in a variable.
        user = db.session.scalar(stmt)
        #If the user exists and the provided password is correct, return a JWT token.
        if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
            token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(hours=3))
            return {"email": user.email, "token": token}
        #Otherwise return an error.
        else:
            return {"error": "Invalid email or password"}, 401
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404
