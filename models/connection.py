from init import db, ma
from marshmallow import fields
from sqlalchemy.orm import relationship

class Connection(db.Model):
    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    friend1_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    friend2_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    friend1 = relationship("User", foreign_keys=[friend1_id])
    friend2 = relationship("User", foreign_keys=[friend2_id])

class ConnectionSchema(ma.Schema):

    class Meta:
        fields = ("id", "friend1_id", "friend2_id")

connection_schema = ConnectionSchema()

connections_schema = ConnectionSchema(many=True)