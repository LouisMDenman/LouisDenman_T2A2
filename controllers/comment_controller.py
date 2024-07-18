from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db, TIME
from models.comment import Comment, comment_schema, comments_schema
from models.grocery_list import GroceryList

comments = Blueprint("comments", __name__)

@comments.route("/grocery_list/<int:list_id>/comments", methods=["POST"])
@jwt_required()
def create_comment(list_id):
    body_data = request.get_json()
    stmt = db.select(GroceryList).filter_by(list_id=list_id)
    grocery_list = db.session.scalar(stmt)
    if grocery_list:
        comment = Comment(
            message = body_data.get("message"),
            timestamp = TIME.strftime("%H:%M:%D"),
            grocery_list = grocery_list,
            user_id = get_jwt_identity()
        )

        db.session.add(comment)
        db.session.commit()

        return comment_schema.dump(comment), 201
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404
    
@comments.route("/grocery_list/<int:list_id>/comments/<int:comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(list_id, comment_id):
    stmt = db.select(Comment).filter_by(comment_id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return {"message": f"Comment '{comment.message}' has been deleted successfully"}
    else:
        return {"error": f"Comment with comment_id {comment_id} not found"}, 404
    
@comments.route("/grocery_list/<int:list_id>/comments/<int:comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_comment(list_id, comment_id):
    body_data = request.get_json()
    stmt = db.select(Comment).filter_by(comment_id=comment_id)
    comment = db.session.scalar(stmt)
    if comment:
        comment.message = body_data.get("message") or comment.message
        comment.timestamp = TIME.strftime("%H:%M:%D")
        db.session.commit()
        return comment_schema.dump(comment)
    else:
        return {"error": f"Comment with id '{comment_id}' not found"}, 404