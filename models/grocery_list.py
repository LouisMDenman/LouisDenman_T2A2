#Third party imports
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

#Local application imports
from init import db, ma

#Establish the Grocery List object/table.
class GroceryList(db.Model):
    #Name of the table.
    __tablename__ = "grocery_lists"

    #Table column names and attributes.
    list_id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    #Relationships with other tables that backfill this table, so that the relevant information from those tables can be displayed through these attributes.
    user = db.relationship("User", back_populates="grocery_list")
    comments = db.relationship("Comment", back_populates="grocery_list", cascade="all,delete")
    product_list = db.relationship("ProductList", back_populates="grocery_list")

#Establish the Grocery List schema.
class GroceryListSchema(ma.Schema):

    #Define what is displayed from the relevant attribtues.
    user = fields.Nested("UserSchema", only=["user_id", "display_name", "email"])
    comments = fields.List(fields.Nested("CommentSchema", exclude=["grocery_list"]))
    product_list = fields.List(fields.Nested("ProductListSchema", exclude=["grocery_list"]))

    #Validate list name input.
    list_name = fields.String(required=True, validate=And(
        Length(min=3, error="List name must be a minimum 3 characters long."),
        Regexp("^[A-Za-z0-9 ]+$", error="Only alphanumeric characters allowed in grocery list names.")
        ))

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("list_id", "list_name", "user", "product_list", "comments")

#Schema object for a single database row.
grocery_list_schema = GroceryListSchema()

#Schema object for multiple database rows.
grocery_lists_schema = GroceryListSchema(many=True)