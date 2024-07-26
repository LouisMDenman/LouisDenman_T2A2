from init import db, ma
from marshmallow import fields

class GroceryList(db.Model):
    __tablename__ = "grocery_lists"

    list_id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    user = db.relationship("User", back_populates="grocery_list")
    comments = db.relationship("Comment", back_populates="grocery_list", cascade="all,delete")
    product_list = db.relationship("ProductList", back_populates="grocery_list")

class GroceryListSchema(ma.Schema):

    user = fields.Nested("UserSchema", only=["user_id", "display_name", "email"])
    comments = fields.List(fields.Nested("CommentSchema", exclude=["grocery_list"]))
    product_list = fields.List(fields.Nested("ProductListSchema", exclude=["grocery_list"]))

    class Meta:
        fields = ("list_id", "list_name", "user", "comments", "product_list")

grocery_list_schema = GroceryListSchema()
grocery_lists_schema = GroceryListSchema(many=True)