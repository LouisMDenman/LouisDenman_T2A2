from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_CATEGORIES = ("Fruits & Vegetables", "Meat & Dairy", "Carbohydrates", "Miscellaneous", "Other")

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float, nullable=False)

    product_list = db.relationship("ProductList", back_populates="products")

class ProductSchema(ma.Schema):

    product_list = fields.Nested("ProductListSchema")

    product_category = fields.String(validate=OneOf(VALID_CATEGORIES), error="Product category must be one of: 'Fruits & Vegetables', 'Meat & Dairy', 'Carbohydrates', 'Miscellaneous', 'Other'.")

    class Meta:
        fields = ("product_id", "product_category", "product_name", "product_price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)