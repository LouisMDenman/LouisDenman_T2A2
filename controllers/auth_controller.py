from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from models.user import User, user_schema
from init import bcrypt, db
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def register_user():
    try:
        body_data = request.get_json()

        user = User(
            first_name = body_data.get("first_name"),
            last_name = body_data.get("last_name"),
            display_name = body_data.get("display_name"),
            email = body_data.get("email")
        )

        password = body_data.get("password")
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "That email is already in use, please try another email."}, 409
        
@auth.route("/login", methods=["POST"])
def user_login():
    body_data = request.get_json()
    stmt = db.Select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(hours=3))
        return {"email": user.email, "token": token}
    else:
        return {"error": "Invalid email or password"}, 401
