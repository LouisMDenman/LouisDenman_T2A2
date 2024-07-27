#Third party imports
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

#Local application imports
from init import db
from models.product_list import ProductList
from models.grocery_list import GroceryList, grocery_list_schema

#Create a Product List Blueprint for the app.
product_list = Blueprint("product_list", __name__)

#Route that handles adding an item/s to a grocery list.
@product_list.route("/add_to_grocery_list/<int:list_id>", methods=["POST"])
#Get user identity:
@jwt_required()
def new_product_list(list_id):
    #Retrieve JSON data.
    body_data = request.get_json()
    #Create a statement that will find a grocery list based on its list_id.
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    #Retrieve this row from the database and store it in a variable.
    grocery_list = db.session.scalar(stmt)
    #If there is a row that matches the provided list_id.
    if grocery_list:
        #Create a new Product List row with the provided JSON data.
        product_list = ProductList(
        quantity = body_data.get("quantity"),
        product_id = body_data.get("product_id"),
        list_id = list_id
        )
        #Add this Product List to the database and show the updated grocery list.
        db.session.add(product_list)
        db.session.commit()
        return grocery_list_schema.dump(grocery_list)
    #Otherwise return an error saying that the list cannot be located.
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404

#Route that handles removing item/s from a grocery list.
@product_list.route("/remove_from_grocery_list/<int:list_id>", methods=["DELETE"])
#Get user identity:
@jwt_required()
def delete_product_list(list_id):
    #Retrieve JSON data.
    body_data = request.get_json()
    #Create a statement that will find a grocery list based on its list_id.
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    #Retrieve this row from the database and store it in a variable.
    grocery_list = db.session.scalar(stmt)
    #If there is a row that matches the provided list_id.
    if grocery_list:
        #Create a statement that will find the product list based on its id.
        stmt = db.select(ProductList).filter_by(id=body_data.get("id"))
        #Retrieve this row from the database and store it in a variable.
        product_list = db.session.scalar(stmt)
        #Remove this Product List from the database and show the updated grocery list.
        db.session.delete(product_list)
        db.session.commit()
        return grocery_list_schema.dump(grocery_list) 
    #Otherwise return an error saying that the list cannot be located.
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404