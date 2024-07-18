from init import db, ma
from marshmallow import fields

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
    connections = db.relationship("Connection", back_populates="user")

class UserSchema(ma.Schema):

    grocery_list = fields.List(fields.Nested("GroceryListSchema"), exclude=["user"])
    comments = fields.List(fields.Nested("CommentSchema", exclude=["user"]))
    connections = fields.List(fields.Nested("ConnectionSchema", exclude=["user"]))

    class Meta:
        fields = ("user_id", "first_name", "last_name", "display_name", "email", "password", "grocery_list", "comments", "connections")

user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])