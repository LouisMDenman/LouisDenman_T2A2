from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.grocery_list import GroceryList, grocery_list_schema, grocery_lists_schema

grocery_list = Blueprint("grocery_lists", __name__)

@grocery_list.route("/grocery_lists")
def get_grocery_lists():
    stmt = db.select(GroceryList)
    g_lists = db.session.scalars(stmt)
    return grocery_lists_schema.dump(g_lists)

@grocery_list.route("/grocery_list/<int:list_id>")
def one_grocery_list(list_id):
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    g_list = db.session.scalar(stmt)
    if g_list:
        return grocery_list_schema.dump(g_list)
    else:
        return {"error": f"Grocery List with id {list_id} not found"}, 404
    
@grocery_list.route("/create_grocery_list", methods=["POST"])
@jwt_required()
def create_grocery_list():
    body_data = request.get_json()
    grocery_list = GroceryList(
        list_name = body_data.get("list_name"),
        user_id = get_jwt_identity()
    )

    db.session.add(grocery_list)
    db.session.commit()

    return grocery_list_schema.dump(grocery_list)

@grocery_list.route("/delete_grocery_list/<int:list_id>", methods=["DELETE"])
@jwt_required()
def delete_grocery_list(list_id):
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    grocery_list = db.session.scalar(stmt)
    if grocery_list:
        db.session.delete(grocery_list)
        db.session.commit()
        return {"message": f"Grocery List '{grocery_list.list_name}' deleted successfully."}
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    
@grocery_list.route("/update_grocery_list_name/<int:list_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_grocery_list(list_id):
    body_data = request.get_json()
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    grocery_list = db.session.scalar(stmt)
    if grocery_list:
        grocery_list.list_name = body_data.get("list_name") or grocery_list.list_name
        db.session.commit()
        return grocery_list_schema.dump(grocery_list)
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404