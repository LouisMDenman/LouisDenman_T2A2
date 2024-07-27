from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.product import Product, product_schema, products_schema

product = Blueprint("product", __name__)

@product.route("/products")
def get_all_products():
    stmt = db.select(Product)
    product = db.session.scalars(stmt)
    return products_schema.dump(product)

@product.route("/products/<int:product_id>")
def one_product(product_id):
    stmt = db.select(Product).filter_by(product_id=product_id)
    product = db.session.scalar(stmt)
    if product:
        return product_schema.dump(product)
    else:
        return {"error": f"Grocery List with id {product_id} not found"}, 404
    
@product.route("/custom_product", methods=["POST"])
def create_product():
    body_data = product_schema.load(request.get_json())
    product = Product(
        product_category = body_data.get("product_category"),
        product_name = body_data.get("product_name"),
        product_price = body_data.get("product_price")
    )

    db.session.add(product)
    db.session.commit()

    return product_schema.dump(product)