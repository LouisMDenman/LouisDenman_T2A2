#Third party imports
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

#Local application imports
from init import db
from models.grocery_list import GroceryList, grocery_list_schema, grocery_lists_schema
from controllers.comment_controller import comments

#Create a Grocery List Blueprint for the app.
grocery_list = Blueprint("grocery_lists", __name__)

#Route that handles displaying all grocery lists
@grocery_list.route("/grocery_lists")
def get_grocery_lists():
    try:
        #Create a statement that will find all grocery lists.
        stmt = db.select(GroceryList)
        #Retrieve these rows from the database and store them in a variable.
        g_lists = db.session.scalars(stmt)
        #Return these rows data
        return grocery_lists_schema.dump(g_lists)
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404

#Route that handles viewing a specific grocery list
@grocery_list.route("/grocery_list/<int:list_id>")
def one_grocery_list(list_id):
    try:
        #Create a statement that will find a grocery list based on its list_id.
        stmt = db.select(GroceryList).filter_by(list_id=list_id)
        #Retrieve this row from the database and store it in a variable.
        g_list = db.session.scalar(stmt)
        #If there is a row that matches the provided list_id.
        if g_list:
            #Return the specific grocery list
            return grocery_list_schema.dump(g_list)
        #Otherwise return an error saying that the list cannot be located.
        else:
            return {"error": f"Grocery List with id {list_id} not found"}, 404
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404

#Route that handles the creation of a new grocery list
@grocery_list.route("/create_grocery_list", methods=["POST"])
#Get user identity:
@jwt_required()
def create_grocery_list():
    try:
        #Retrieve JSON data.
        body_data = grocery_list_schema.load(request.get_json())
        #Create a new Grocery List row with the provided JSON data.
        grocery_list = GroceryList(
            list_name = body_data.get("list_name"),
            user_id = get_jwt_identity()
        )

        #Add this Grocery List to the database and show the new grocery list.
        db.session.add(grocery_list)
        db.session.commit()

        return grocery_list_schema.dump(grocery_list)
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404

#Route that handles deleting existing grocery lists
@grocery_list.route("/delete_grocery_list/<int:list_id>", methods=["DELETE"])
#Get user identity:
@jwt_required()
def delete_grocery_list(list_id):
    try:
        #Create a statement that will find a grocery list based on its list_id.
        stmt = db.select(GroceryList).filter_by(list_id=list_id)
        #Retrieve this row from the database and store it in a variable.
        grocery_list = db.session.scalar(stmt)
        #If there is a row that matches the provided list_id.
        if grocery_list:
            #Remove this Grocery List from the database and provide a confirmation message.
            db.session.delete(grocery_list)
            db.session.commit()
            return {"message": f"Grocery List '{grocery_list.list_name}' deleted successfully."}
        #Otherwise return an error saying that the list cannot be located.
        else:
            return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404
    
#Route for handling the update of a grocery list name.
@grocery_list.route("/update_grocery_list_name/<int:list_id>", methods=["PUT", "PATCH"])
#Get user identity:
@jwt_required()
def update_grocery_list(list_id):
    try:
        #Retrieve JSON data.
        body_data = grocery_list_schema.load(request.get_json())
        #Create a statement that will find a grocery list based on its list_id.
        stmt = db.select(GroceryList).filter_by(list_id=list_id)
        #Retrieve this row from the database and store it in a variable.
        grocery_list = db.session.scalar(stmt)
        #If there is a row that matches the provided list_id.
        if grocery_list:
            #Update the list_name field of the grocery list, add this name to the database and return the renamed grocery list
            grocery_list.list_name = body_data.get("list_name") or grocery_list.list_name
            db.session.commit()
            return grocery_list_schema.dump(grocery_list)
        #Otherwise return an error saying that the list cannot be located.
        else:
            return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404