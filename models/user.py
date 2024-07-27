from init import db, ma
from marshmallow import fields
from sqlalchemy.orm import relationship
from marshmallow.validate import Regexp

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    grocery_list = db.relationship("GroceryList", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    connections = relationship("Connection", primaryjoin="or_(User.user_id==Connection.friend1_id, User.user_id==Connection.friend2_id)", viewonly=True)

class UserSchema(ma.Schema):

    grocery_list = fields.List(fields.Nested("GroceryListSchema"), exclude=["user"])
    comments = fields.List(fields.Nested("CommentSchema", exclude=["user"]))
    connections = fields.List(fields.Nested("ConnectionSchema", exclude=["user"]))

    email = fields.String(required=True, validate=Regexp(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", error="Invalid email format."))

    password = fields.String(required=True, validate=Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"), error="Password must be a minimum length of eight characters, and contain at least one letter and number.")

    class Meta:
        fields = ("user_id", "first_name", "last_name", "display_name", "email", "password", "grocery_list", "comments", "connections")

user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])