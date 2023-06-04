"""Data models."""
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from database import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "user"
    Userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    ShoppingCartID = db.Column(db.Integer)
    Address = db.Column(db.Integer)
    isAdmin = db.Column(db.Boolean)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.isAdmin = kwargs.get("adminPassword")
        print("isAdmin: ", self.isAdmin)


    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.email)

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database

        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)
    
class ProductType(db.Model):
    """Data model for product types."""

    __tablename__ = "product_type"
    ProductTypeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        self.Name = kwargs.get("Name")


class Product(db.Model):
    """Data model for products."""

    __tablename__ = "product"
    ProductID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    SetNo = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(250), nullable=False)
    Image = db.Column(db.String(50), nullable = False)
    Availability = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)
    PieceCount = db.Column(db.Integer, nullable=False)
    ProductTypeID = db.Column(db.Integer, db.ForeignKey('product_type.ProductTypeID'), nullable=False)

    def __init__(self, **kwargs):
        self.Name = kwargs.get("Name")
        self.SetNo = kwargs.get("SetNo")
        self.Price = kwargs.get("Price")
        self.Description = kwargs.get("Description")
        self.Image = kwargs.get("Image")
        self.Availability = kwargs.get("Availability")
        self.ReleaseDate = kwargs.get("ReleaseDate")
        self.PieceCount = kwargs.get("PieceCount")
        self.ProductTypeID = kwargs.get("ProductTypeID")


class Set(db.Model):
    """Data model for sets."""

    __tablename__ = "set"
    SetID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    SetNo = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(250), nullable=False)
    ImagePath = db.Column(db.String(255), nullable=False)
    Availability = db.Column(db.Integer, nullable=False)
    UnitsSold = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)
    PieceCount = db.Column(db.Integer, nullable=False)
    Instruction = db.Column(db.Text, nullable=False)

    def __init__(self, **kwargs):
        self.Name = kwargs.get("Name")
        self.SetNo = kwargs.get("SetNo")
        self.Price = kwargs.get("Price")
        self.Description = kwargs.get("Description")
        self.ImagePath = kwargs.get("ImagePath")
        self.Availability = kwargs.get("Availability")
        self.UnitsSold = kwargs.get("UnitsSold")
        self.ReleaseDate = kwargs.get("ReleaseDate")
        self.PieceCount = kwargs.get("PieceCount")
        self.Instruction = kwargs.get("Instruction")

class ShoppingCart(db.Model):
    """Data model for shopping carts."""

    __tablename__ = "shopping_cart"
    ShoppingCartID = db.Column(db.Integer, primary_key=True)
    ShippingCost = db.Column(db.Integer, nullable=False)
    NumberOfItems = db.Column(db.Integer, nullable=False)
    TotalPrice = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.ShippingCost = kwargs.get("ShippingCost")
        self.NumberOfItems = kwargs.get("NumberOfItems")
        self.TotalPrice = kwargs.get("TotalPrice")

class Address(db.Model):
    """Data model for addresses."""

    __tablename__ = "address"
    AddressID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    City = db.Column(db.String(50))
    StreetName = db.Column(db.String(50))
    StreetNo = db.Column(db.String(10))
    AppartmentNo = db.Column(db.String(10))
    PostCode = db.Column(db.String(10))

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.country = kwargs.get("country")
        self.city = kwargs.get("city")
        self.street_name = kwargs.get("street_name")
        self.street_no = kwargs.get("street_no")
        self.apartment_no = kwargs.get("apartment_no")
        self.post_code = kwargs.get("post_code")

class ShoppingCart_Product(db.Model):
    """Data model for shopping cart products."""

    __tablename__ = "shoppingcart_product"
    ShoppingCartProductID = db.Column(db.Integer, primary_key=True)
    ShoppingCartID = db.Column(db.Integer, db.ForeignKey("shopping_cart.ShoppingCartID"))
    ProductID = db.Column(db.Integer, db.ForeignKey("product.ProductID"))
    SetID = db.Column(db.Integer, db.ForeignKey("set.SetID"))
    __table_args__ = (
        db.CheckConstraint("ProductID IS NOT NULL OR SetID IS NOT NULL"),
    )

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.shopping_cart_id = kwargs.get("shopping_cart_id")
        self.product_id = kwargs.get("product_id")
        self.set_id = kwargs.get("set_id")

class Set_Product(db.Model):
    """Data model for set products."""

    __tablename__ = "set_product"
    SetProductID = db.Column(db.Integer, primary_key=True)
    SetID = db.Column(db.Integer, db.ForeignKey("set.SetID"))
    ProductID = db.Column(db.Integer, db.ForeignKey("product.ProductID"))

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.set_id = kwargs.get("set_id")
        self.product_id = kwargs.get("product_id")

class BuyingHistory(db.Model):
    """Data model for buying history."""

    __tablename__ = "buyinghistory"
    BuyingHistoryID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey("user.Userid"))
    ShoppingCartID = db.Column(db.Integer, db.ForeignKey("shopping_cart.ShoppingCartID"))
    DateOfPurchase = db.Column(db.Date)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.user_id = kwargs.get("user_id")
        self.shopping_cart_id = kwargs.get("shopping_cart_id")
        self.date_of_purchase = kwargs.get("date_of_purchase")

class Tag(db.Model):
    __tablename__ = "tag"
    TagID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        self.Name = kwargs.get("Name")

class Product_Tag(db.Model):

    __tablename__="product_tag"
    ProductTagID = db.Column(db.Integer, primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey("product.ProductID"))
    TagID =  db.Column(db.Integer, db.ForeignKey("tag.TagID"))

    def __init__(self, **kwargs):

        self.ProductID = kwargs.get("product_id")
        self.TagID = kwargs.get("tag_id")
