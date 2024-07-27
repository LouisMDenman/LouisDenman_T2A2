#Third party imports
from marshmallow import fields

#Local application imports
from init import db, ma

#Establish the Product List object/table.
class ProductList(db.Model):
    #Name of the table.
    __tablename__ = "product_list"

    #Table column names and attributes.
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("grocery_lists.list_id"), nullable=False)

    #Relationships with other tables that backfill this table, so that the relevant information from those tables can be displayed through these attributes.
    products = db.relationship("Product", back_populates="product_list")
    grocery_list = db.relationship("GroceryList", back_populates="product_list")

#Establish the Product List schema.
class ProductListSchema(ma.Schema):

    #Define what is displayed from the relevant attribtues.
    products = fields.Nested("ProductSchema", only=["product_id", "product_name", "product_price"])
    grocery_list = fields.Nested("GroceryListSchema", only=["list_name"])

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("id", "products", "quantity", "grocery_list")

#Schema object for a single database row.
product_list_schema = ProductListSchema()

#Schema object for multiple database rows.
product_lists_schema = ProductListSchema(many=True)