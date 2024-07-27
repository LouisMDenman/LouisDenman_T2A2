#Third party imports
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

#Local application imports
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
    stmt = db.select(Connection)
    friend = db.session.scalars(stmt)

    for instance in friend:
        if (str(instance.friend1_id) == str(get_jwt_identity())) and (str(instance.friend2_id) == str(friend_id)) or (str(instance.friend1_id) == str(friend_id)) and (str(instance.friend2_id) == str(get_jwt_identity())):
            return {"error": "You are already friends with this user."}, 404
            
    new_connection = Connection(
        friend1_id = get_jwt_identity(),
        friend2_id = friend_id
        )

    db.session.add(new_connection)
    db.session.commit()

    return connection_schema.dump(new_connection)

@connections.route("/remove_connection/<int:friend_id>", methods=["DELETE"])
@jwt_required()
def remove_connection(friend_id):
    stmt = db.select(Connection)
    friend = db.session.scalars(stmt)

    for instance in friend:
        if (str(instance.friend1_id) == str(get_jwt_identity())) and (str(instance.friend2_id) == str(friend_id)) or (str(instance.friend1_id) == str(friend_id)) and (str(instance.friend2_id) == str(get_jwt_identity())):
            stmt = db.select(Connection).filter_by(id=instance.id)
            conn = db.session.scalar(stmt)
            db.session.delete(conn)
            db.session.commit()
            return {"message": "This connection has been removed."}

    return {"error": "You are not connected with this user or the user cannot be found."}, 404
    
