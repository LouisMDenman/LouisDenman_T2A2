from flask import Blueprint

from init import db, bcrypt, TIME
from models.user import User
from models.grocery_list import GroceryList
from models.comment import Comment
from models.connection import Connection
from models.product import Product
from models.product_list import ProductList

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

    connections = [
        Connection(
            friend1_id = "1",
            friend2_id = "2"
        ),
        Connection(
            friend1_id = "3",
            friend2_id = "2"
        )
    ]

    db.session.add_all(connections)

    products = [
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Tomato",
            product_price = 1.5
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Capsicum",
            product_price = 2
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Apple",
            product_price = 1
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Banana",
            product_price = 1.5
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Orange",
            product_price = 2
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Watermelon",
            product_price = 4
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Lemon",
            product_price = 1.7
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Coconut",
            product_price = 5
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Cucumber",
            product_price = 1
        ),
        Product(
            product_category = "Fruits & Vegetables",
            product_name = "Eggplant",
            product_price = 1.5
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Beef",
            product_price = 7
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Turkey",
            product_price = 6.5
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Chicken",
            product_price = 7
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Pork",
            product_price = 9
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Bacon",
            product_price = 7
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Cheddar Cheese",
            product_price = 4
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Shredded Cheese",
            product_price = 5
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Light Milk",
            product_price = 6
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Full Cream Milk",
            product_price = 5
        ),
        Product(
            product_category = "Meat & Dairy",
            product_name = "Cottage Cheese",
            product_price = 3
        ),
        Product(
            product_category = "Carbohydrates",
            product_name = "White Rice",
            product_price = 4
        ),
        Product(
            product_category = "Carbohydrates",
            product_name = "Brown Rice",
            product_price = 5
        ),
        Product(
            product_category = "Carbohydrates",
            product_name = "Pasta",
            product_price = 4
        ),
        Product(
            product_category = "Carbohydrates",
            product_name = "Bread",
            product_price = 3
        ),
        Product(
            product_category = "Carbohydrates",
            product_name = "Tortillas",
            product_price = 4
        ),
        Product(
            product_category = "Miscellaneous",
            product_name = "Knife Set",
            product_price = 10
        ),
        Product(
            product_category = "Miscellaneous",
            product_name = "Cutting Board",
            product_price = 8
        ),
        Product(
            product_category = "Miscellaneous",
            product_name = "Containers",
            product_price = 15
        ),
        Product(
            product_category = "Miscellaneous",
            product_name = "Baking Pack",
            product_price = 20
        ),
        Product(
            product_category = "Miscellaneous",
            product_name = "Magazine",
            product_price = 5
        )
    ]

    db.session.add_all(products)

    product_lists = [
        ProductList(
            quantity = 5,
            products = products[5],
            grocery_list = grocery_lists[1]
        ),
        ProductList(
            quantity = 3,
            products = products[8],
            grocery_list = grocery_lists[1]
        ),
        ProductList(
            quantity = 2,
            products = products[13],
            grocery_list = grocery_lists[1]
        ),
        ProductList(
            quantity = 7,
            products = products[23],
            grocery_list = grocery_lists[1]
        ),
        ProductList(
            quantity = 1,
            products = products[29],
            grocery_list = grocery_lists[1]
        ),
        ProductList(
            quantity = 6,
            products = products[9],
            grocery_list = grocery_lists[2]
        ),
        ProductList(
            quantity = 2,
            products = products[11],
            grocery_list = grocery_lists[2]
        ),
        ProductList(
            quantity = 6,
            products = products[19],
            grocery_list = grocery_lists[2]
        ),
        ProductList(
            quantity = 4,
            products = products[21],
            grocery_list = grocery_lists[2]
        ),
        ProductList(
            quantity = 1,
            products = products[27],
            grocery_list = grocery_lists[2]
        )
    ]

    db.session.add_all(product_lists)

    db.session.commit()

    print("tables seeded succesfully")