#Third party imports
from marshmallow import fields
from marshmallow.validate import OneOf

#Local application imports
from init import db, ma

#Constant which contains tuple of allowed product categories.
VALID_CATEGORIES = ("Fruits & Vegetables", "Meat & Dairy", "Carbohydrates", "Miscellaneous", "Other")

#Establish the Product object/table
class Product(db.Model):
    #Name of the table.
    __tablename__ = "products"

    #Table column names and attributes.
    product_id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float, nullable=False)

    #Relationships with other tables that backfill this table, so that the relevant information from those tables can be displayed through these attributes.
    product_list = db.relationship("ProductList", back_populates="products")

#Establish the User schema.
class ProductSchema(ma.Schema):

    #Define what is displayed from the relevant attribtues.
    product_list = fields.Nested("ProductListSchema")

    #Validate product category input.
    product_category = fields.String(validate=OneOf(VALID_CATEGORIES), error="Product category must be one of: 'Fruits & Vegetables', 'Meat & Dairy', 'Carbohydrates', 'Miscellaneous', 'Other'.")

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("product_id", "product_category", "product_name", "product_price")

#Schema object for a single database row.
product_schema = ProductSchema()

#Schema object for multiple database rows.
products_schema = ProductSchema(many=True)