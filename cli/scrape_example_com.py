import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/dbname"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    source_id = db.Column(db.Integer, db.ForeignKey("source.id"), nullable=False)

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    products = db.relationship("Product", backref="source", lazy=True)

with app.app_context():
    db.create_all()

    # Replace the URL below with the URL of the product detail page you want to scrape
    url = "https://example.com/product-detail-page"

    # Send an HTTP request to the URL and parse the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Replace the selectors below with the appropriate class or ID for the HTML tags on the target webshop
    title_selector = ".title-class"
    description_selector = "#description-id"
    price_selector = ".price-class"
    image_url_selector = "#image-url-id"

    # Extract data from the HTML tags using the selectors
    title = soup.select_one(title_selector).text.strip()
    description = soup.select_one(description_selector).text.strip()
    price = float(soup.select_one(price_selector).text.strip().replace("$", ""))
    image_url = soup.select_one(image_url_selector)["src"]

    # Get the source ID for the current webshop (you can replace 1 with the actual source ID)
    source_id = 1

    # Create a new product object with the extracted data
    product = Product(title=title, description=description, price=price, image_url=image_url, source_id=source_id)

    # Add the product to the database and commit the changes
    db.session.add(product)
    db.session.commit()

    print("Product added to the database.")
