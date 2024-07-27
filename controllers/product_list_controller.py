from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.product_list import ProductList, product_list_schema, product_lists_schema
from models.grocery_list import GroceryList, grocery_list_schema

product_list = Blueprint("product_list", __name__)

@product_list.route("/add_to_grocery_list/<int:list_id>", methods=["POST"])
@jwt_required()
def new_product_list(list_id):
    body_data = request.get_json()
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    grocery_list = db.session.scalar(stmt)
    if grocery_list:

        product_list = ProductList(
        quantity = body_data.get("quantity"),
        product_id = body_data.get("product_id"),
        list_id = list_id
        )

        db.session.add(product_list)
        db.session.commit()
        return grocery_list_schema.dump(grocery_list)
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    
@product_list.route("/remove_from_grocery_list/<int:list_id>", methods=["DELETE"])
@jwt_required()
def delete_product_list(list_id):
    body_data = request.get_json()
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    grocery_list = db.session.scalar(stmt)
    if grocery_list:
        stmt = db.select(ProductList).filter_by(id=body_data.get("id"))
        product_list = db.session.scalar(stmt)
        db.session.delete(product_list)
        db.session.commit()
        return grocery_list_schema.dump(grocery_list) 
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404