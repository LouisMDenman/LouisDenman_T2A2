#Third party imports
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

#Local application imports
from init import db
from models.connection import Connection, connection_schema, connections_schema

#Create a Connection Blueprint for the app.
connections = Blueprint("connections", __name__)

#Route that handles viewing users connections.
@connections.route("/connections")
@jwt_required()
def view_connections():
    stmt = db.select(Connection)
    conns = db.session.scalars(stmt)
    return connections_schema.dump(conns)

#Route that handles adding new connections.
@connections.route("/new_connection/<int:friend_id>", methods=["POST"])
#Get user identity:
@jwt_required()
def add_connection(friend_id):
    #Create a statement that selects all connections.
    stmt = db.select(Connection)
    #Retrieve these rows from the database and store them in a variable.
    friend = db.session.scalars(stmt)

    #Loop through each row of the database.
    for instance in friend:
        #Check if the current user and desired connection are already friends in the particular row.
        if (str(instance.friend1_id) == str(get_jwt_identity())) and (str(instance.friend2_id) == str(friend_id)) or (str(instance.friend1_id) == str(friend_id)) and (str(instance.friend2_id) == str(get_jwt_identity())):
            #If they are, return an error stating that the connection already exists.
            return {"error": "You are already friends with this user."}, 404
    
    #Create a new connection row in the database.
    new_connection = Connection(
        friend1_id = get_jwt_identity(),
        friend2_id = friend_id
        )

    db.session.add(new_connection)
    db.session.commit()

    #Return the new connection.
    return connection_schema.dump(new_connection)

#Route that handles removing a connection.
@connections.route("/remove_connection/<int:friend_id>", methods=["DELETE"])
#Get user identity:
@jwt_required()
def remove_connection(friend_id):
    #Create a statement that selects all connections.
    stmt = db.select(Connection)
    #Retrieve these rows from the database and store them in a variable.
    friend = db.session.scalars(stmt)

    #Loop through each row of the database.
    for instance in friend:
        #Check if the current user and desired connection are already friends in the particular row.
        if (str(instance.friend1_id) == str(get_jwt_identity())) and (str(instance.friend2_id) == str(friend_id)) or (str(instance.friend1_id) == str(friend_id)) and (str(instance.friend2_id) == str(get_jwt_identity())):
            #If they are, create a statement that will select this row from the database, store it in a variable and delete the row in the database as well as return a confirmation message.
            stmt = db.select(Connection).filter_by(id=instance.id)
            conn = db.session.scalar(stmt)
            db.session.delete(conn)
            db.session.commit()
            return {"message": "This connection has been removed."}

    #Return an error stating that the connection doesn't exist or can't be found.
    return {"error": "You are not connected with this user or the user cannot be found."}, 404
    
