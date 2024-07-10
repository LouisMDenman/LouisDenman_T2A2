from init import db, ma

class User(db.Model):
    __tablename__ = "USERS"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "first_name", "last_name", "display_name", "email", "password")

user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])