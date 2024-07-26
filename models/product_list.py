from init import db, ma
from marshmallow import fields

class ProductList(db.Model):
    __tablename__ = "product_list"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("grocery_lists.list_id"), nullable=False)

    products = db.relationship("Product", back_populates="product_list")
    grocery_list = db.relationship("GroceryList", back_populates="product_list")

class ProductListSchema(ma.Schema):

    product = fields.Nested("ProductSchema")
    grocery_list = fields.Nested("GroceryListSchema", only=["list_name"])

    class Meta:
        fields = ("id", "products", "quantity", "list_id", "grocery_list")

product_list_schema = ProductListSchema()
product_lists_schema = ProductListSchema(many=True)