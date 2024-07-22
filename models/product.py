from init import db, ma

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    product_price = db.Column(db.Float, nullable=False)

class ProductSchema(ma.Schema):

    class Meta:
        fields = ("product_id", "product_category", "product_name", "product_price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)