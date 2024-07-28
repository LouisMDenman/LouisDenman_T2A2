#Third party imports
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

#Local application imports
from init import db, TIME
from models.comment import Comment, comment_schema
from models.grocery_list import GroceryList

#Create a Comments Blueprint for the app.
comments = Blueprint("comments", __name__)

#Route that handles creating comments.
@comments.route("/grocery_list/<int:list_id>/comments", methods=["POST"])
#Get user identity:
@jwt_required()
def create_comment(list_id):
    #Retrieve JSON data.
    body_data = request.get_json()
    #Create a statement that will find a grocery list based on its list_id.
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    #Retrieve this row from the database and store it in a variable.
    grocery_list = db.session.scalar(stmt)
    #If there is a row that matches the provided list_id.
    if grocery_list:
        #Create a new comment row with provided JSON data.
        comment = Comment(
            message = body_data.get("message"),
            timestamp = TIME.strftime("%H:%M:%D"),
            grocery_list = grocery_list,
            user_id = get_jwt_identity()
        )

        #Add this Comment to the database and return the new comment.
        db.session.add(comment)
        db.session.commit()

        return comment_schema.dump(comment), 201
    #Otherwise return an error saying that the list cannot be located.
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    
#Route that handles deleting a comment.
@comments.route("/grocery_list/<int:list_id>/comments/<int:comment_id>", methods=["DELETE"])
#Get user identity:
@jwt_required()
def delete_comment(list_id, comment_id):
    #Create a statement that will find a comment based on its comment_id.
    stmt = db.select(Comment).filter_by(comment_id=comment_id)
    #Retrieve this row from the database and store it in a variable.
    comment = db.session.scalar(stmt)
    #If there is a row that matches the provided comment_id.
    if comment:
        #Remove this Comment from the database and provide a confirmation message.
        db.session.delete(comment)
        db.session.commit()
        return {"message": f"Comment '{comment.message}' has been deleted successfully"}
    #Otherwise return an error saying that the comment cannot be located.
    else:
        return {"error": f"Comment with comment_id {comment_id} not found"}, 404

#Route that handles the editing of comments.
@comments.route("/grocery_list/<int:list_id>/comments/<int:comment_id>", methods=["PUT", "PATCH"])
#Get user identity:
@jwt_required()
def edit_comment(list_id, comment_id):
    #Retrieve JSON data.
    body_data = request.get_json()
    #Create a statement that will find a comment based on its comment_id.
    stmt = db.select(Comment).filter_by(comment_id=comment_id)
    #Retrieve this row from the database and store it in a variable.
    comment = db.session.scalar(stmt)
    #If there is a row that matches the provided comment_id.
    if comment:
        #Update the message and timestamp attributes for the row, copy them into the database and return the updated comment.
        comment.message = body_data.get("message") or comment.message
        comment.timestamp = TIME.strftime("%H:%M:%D")
        db.session.commit()
        return comment_schema.dump(comment)
    #Otherwise return an error saying that the comment cannot be located.
    else:
        return {"error": f"Comment with id '{comment_id}' not found"}, 404