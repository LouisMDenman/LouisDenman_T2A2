#Third party imports
from marshmallow import fields
from sqlalchemy.orm import relationship
from marshmallow.validate import Regexp

#Local application imports
from init import db, ma

#Establish the User object/table.
class User(db.Model):
    #Name of the table.
    __tablename__ = "users"

    #Table column names and attributes.
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    #Relationships with other tables that backfill this table, so that the relevant information from those tables can be displayed through these attributes.
    grocery_list = db.relationship("GroceryList", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    connections = relationship("Connection", primaryjoin="or_(User.user_id==Connection.friend1_id, User.user_id==Connection.friend2_id)", viewonly=True)

#Establish the User schema.
class UserSchema(ma.Schema):

    #Define what is displayed from the relevant attribtues.
    grocery_list = fields.List(fields.Nested("GroceryListSchema"), exclude=["user"])
    comments = fields.List(fields.Nested("CommentSchema", exclude=["user"]))
    connections = fields.List(fields.Nested("ConnectionSchema", exclude=["user"]))

    #Validate email and password input.
    email = fields.String(required=True, validate=Regexp(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", error="Invalid email format."))
    password = fields.String(required=True, validate=Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"), error="Password must be a minimum length of eight characters, and contain at least one letter and number.")

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("user_id", "first_name", "last_name", "display_name", "email", "password", "grocery_list", "comments", "connections")

#Schema object for a single database row.
user_schema = UserSchema(exclude=["password"])

#Schema object for multiple database rows.
users_schema = UserSchema(many=True, exclude=["password"])