from init import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("grocery_lists.list_id"), nullable=False)

    user = db.relationship("User", back_populates="comments")
    grocery_list = db.relationship("GroceryList", back_populates="comments")

class CommentSchema(ma.Schema):

    user = fields.Nested("UserSchema", only=["display_name", "email"])
    grocery_list = fields.Nested("GroceryListSchema", exclude=["comments"])

    class Meta:
        fields = ("comment_id", "message", "timestamp", "user", "grocery_list")

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)