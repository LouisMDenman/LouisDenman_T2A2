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

@connections.route("/new_connection/<int:friend_id>", methods=["POST"])
@jwt_required()
def add_connection(friend_id):
    pass

@connections.route("/remove_connection/<int:friend_id>", methods=["POST"])
@jwt_required()
def remove_connection(friend_id):
    pass
    
