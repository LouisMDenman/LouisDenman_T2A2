#Third party imports
from flask import Blueprint, request

#Local application imports
from init import db
from models.product import Product, product_schema, products_schema

#Create a Product Blueprint for the app.
product = Blueprint("product", __name__)

#Route that handles displaying all the products available.
@product.route("/products")
def get_all_products():
    try:
        #Create a statement that finds all rows of Products.
        stmt = db.select(Product)
        #Retrieve these rows from the database and store them in a variable.
        product = db.session.scalars(stmt)
        #Return all the rows of data.
        return products_schema.dump(product)
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404

#Route that handles displaying a single product row.
@product.route("/products/<int:product_id>")
def one_product(product_id):
    try:
        #Create a statement that finds a product based on its product_id.
        stmt = db.select(Product).filter_by(product_id=product_id)
        #Retrieve this row from the database and store it in a variable.
        product = db.session.scalar(stmt)
        #If there is a row that matches the provided product_id.
        if product:
            #Return the row of data.
            return product_schema.dump(product)
        #Otherwise return an error saying that the list cannot be located.
        else:
            return {"error": f"Grocery List with id {product_id} not found"}, 404
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404
    
#Route that handles the creation of a custom product.
@product.route("/custom_product", methods=["POST"])
def create_product():
    try:
        #Retrieve JSON data.
        body_data = product_schema.load(request.get_json())
        #Create a new Product row with the provided JSON data.
        product = Product(
            product_category = body_data.get("product_category"),
            product_name = body_data.get("product_name"),
            product_price = body_data.get("product_price")
        )
        #Add this Product to the database and show the created product.
        db.session.add(product)
        db.session.commit()

        return product_schema.dump(product)
    except:
        return {"error": "Sorry, unknown error encounted. Contact the API web server creator if issues persist."}, 404