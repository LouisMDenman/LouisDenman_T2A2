from flask import Blueprint

from init import db, bcrypt, TIME
from models.user import User
from models.grocery_list import GroceryList
from models.comment import Comment
from models.connection import Connection

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

    grocery_lists = [
        GroceryList(
            list_name = "Housemates grocery list",
            user = users[0]
        ),
        GroceryList(
            list_name = "Family grocery list",
            user = users[1]
        ),
        GroceryList(
            list_name = "Groceries",
            user = users[1]
        )
    ]

    db.session.add_all(grocery_lists)

    comments = [
        Comment(
            message = "We are making tacos this week, make sure you grab the spice mix",
            timestamp = TIME.strftime("%H:%M:%D"),
            user = users[2],
            grocery_list = grocery_lists[0]
        ),
        Comment(
            message = "grab apples pls thx",
            timestamp = TIME.strftime("%H:%M:%D"),
            user = users[0],
            grocery_list = grocery_lists[1]
        )    
    ]

    db.session.add_all(comments)

    db.session.commit()

    print("tables seeded succesfully")