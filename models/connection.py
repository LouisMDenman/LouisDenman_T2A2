#Third party imports
from sqlalchemy.orm import relationship

#Local application imports
from init import db, ma

#Establish the Connection object/table.
class Connection(db.Model):
    #Name of the table.
    __tablename__ = "connections"

    #Table column names and attributes.
    id = db.Column(db.Integer, primary_key=True)
    friend1_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    friend2_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    #Explicitly state foreign key relationships between friend1_id, friend2_id and user_id to be able to utilise connection routes correctly.
    friend1 = relationship("User", foreign_keys=[friend1_id])
    friend2 = relationship("User", foreign_keys=[friend2_id])

#Establish the Connection schema.
class ConnectionSchema(ma.Schema):

    #State which fields are displayed in the schema.
    class Meta:
        fields = ("id", "friend1_id", "friend2_id")

#Schema object for a single database row.
connection_schema = ConnectionSchema()

#Schema object for multiple database rows.
connections_schema = ConnectionSchema(many=True)