from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.connection import Connection, connection_schema, connections_schema

connections = Blueprint("connections", __name__)

@connections.route("/connections")
@jwt_required()
def view_connections():
    stmt = db.select(Connection)
    conns = db.session.scalars(stmt)
    return connections_schema.dump(conns)

@connections.route("/new_connection/<int:my_id>", methods=["POST"])
@jwt_required()
def add_connection(my_id):
    body_data = request.get_json()
    stmt1 = db.select(Connection).filter_by(friend1_id=my_id)
    stmt2 = db.select(Connection).filter_by(friend2_id=my_id)
    friend1 = db.session.scalar(stmt1)
    friend2 = db.session.scalar(stmt2)

    if friend1:
        if friend1.get("friend2_id") == body_data.get("friend2_id"):
            return {"error": "You already have this person added as a friend."}, 404
    if friend2:
        if friend2.get("friend1_id") == body_data.get("friend1_id"):
            return {"error": "You already have this person added as a friend."}, 404
            
    new_connection = Connection(
        friend1_id = get_jwt_identity(),
        friend2_id = body_data.get("friend2_id")
    )

    db.session.add(new_connection)
    db.session.commit()

    return connection_schema.dump(new_connection)

@connections.route("/remove_connection/<int:friend_id>", methods=["POST"])
@jwt_required()
def remove_connection(friend_id):
    pass
    
