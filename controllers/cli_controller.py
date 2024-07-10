from flask import Blueprint

from init import db, bcrypt
from models.user import User

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables successfully created")

@db_commands.cli.command("drop")
def delete_tables():
    db.drop_all()
    print("Tables deleted successfully")

@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            first_name = "Louis",
            last_name = "Denman",
            display_name = "LouisD",
            email = "LouisDenman@gmail.com",
            password = bcrypt.generate_password_hash("Lou1sdenman!").decode("utf-8")
        ),
        User(
            first_name = "John",
            last_name = "Smith",
            display_name = "Jsmith",
            email = "Johnsmith@gmail.com",
            password = bcrypt.generate_password_hash("Johnnybo1!").decode("utf-8")
        ),
        User(
            first_name = "Mary",
            last_name = "Jane",
            display_name = "MJparker",
            email = "Maryjane@gmail.com",
            password = bcrypt.generate_password_hash("Janemary1!").decode("utf-8")
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print("tables seeded succesfully")