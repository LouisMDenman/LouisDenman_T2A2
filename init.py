#Standard library imports
from datetime import datetime

#Third party imports
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

#Create initial instances of the libraries required, so that there are no issues when initialising the app.
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

#Establish a constant variable for the current datetime, so that any route which requires it can import the variable for DRYer code.
TIME = datetime.now()