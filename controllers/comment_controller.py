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
            user = get_jwt_identity()
        )

        db.session.add(comment)
        db.session.commit()

        return comment_schema.dump(comment), 201
    else:
        return {"error": f"Grocery List with list_id '{list_id}' not found"}, 404