#Third party imports
from marshmallow import fields

#Local application imports
from init import db, ma

#Establish the Comment object/table.
class Comment(db.Model):
    #Name of the table.
    __tablename__ = "comments"

    #Table column names and attributes.
    comment_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("grocery_lists.list_id"), nullable=False)

    #Relationships with other tables that backfill this table, so that the relevant information from those tables can be displayed through these attributes.
    user = db.relationship("User", back_populates="comments")
    grocery_list = db.relationship("GroceryList", back_populates="comments")

#Establish the Comment schema.
class CommentSchema(ma.Schema):

    #Define what is displayed from the relevant attribtues.
    user = fields.Nested("UserSchema", only=["display_name", "email"])
    grocery_list = fields.Nested("GroceryListSchema", exclude=["comments"])

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("comment_id", "message", "timestamp", "user", "grocery_list")

#Schema object for a single database row.
comment_schema = CommentSchema()

#Schema object for multiple database rows.
comments_schema = CommentSchema(many=True)