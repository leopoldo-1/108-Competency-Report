from flask import Flask
import json
from mock_data import mock_catalog

#server. its the name
app = Flask('server')

@app.route("/home") #decorator
def home():
    return "Hello there!!"

@app.route("/") #decorator
def root():
    return "Welcome to the online store server"

########################################################
###################  API  CATALOG  #####################
########################################################

@app.route("/api/about", methods=["POST"])
def about():
  me = {
    "first_name": "Leo",
    "last_name": "Miranda"
  }

  return json.dumps(me)
# -------------------------------

@app.route("/api/catalog")
def get_catalog():
  return json.dumps(mock_catalog)
# -------------------------------

@app.route("/api/catalog/cheapest")
def get_cheapest():
  cheapest = mock_catalog[0]

  for product in mock_catalog:
    if(product["price"] < cheapest["price"]):
      cheapest = product

  return json.dumps(cheapest)
  # return(f"The cheapest product is: {cheapest['title']} - Price: ${cheapest['price']}")

@app.route("/api/catalog/sum")
def get_sum_all_products():

  total = 0

  for product in mock_catalog:
    total += product["price"]

  return (f"the total is: {total} ")

#find a product based on the unique id
@app.route("/api/product/<id>")
def find_product(id):

  for product in mock_catalog:
    print('product..',product["_id"])
    if(id == product['_id']):
      return json.dumps(product)

# get the list of categories from the catalog
# /api/products/categories
# expected: a list of strings containing the prods categories
@app.route("/api/products/categories")
def find_categories():
  list_of_categories = []

  for product in mock_catalog:
    cat = product["category"]

    if cat not in list_of_categories:
      list_of_categories.append(cat)

    # if(len(list_of_categories) < 1):
    #   list_of_categories.append(cat)
    # else:
    #    for categorie in list_of_categories:
    #      if(categorie != cat):
    #        list_of_categories.append(cat)
    #        break
  return json.dumps(list_of_categories)

# get all the products that belong to an specified category
# /api/products/category/Coffee
@app.route("/api/products/category/<cat_name>")
def get_by_category(cat_name):

  list_of_products = []

  for product in mock_catalog:
    prod = product['category']

    if(prod.lower() == cat_name.lower()):
      list_of_products.append(product)

  return json.dumps(list_of_products)

# search by text INSIDE the title
# receive a text
# return all product whose title contains the text
@app.route("/api/products/search/<text>")
def search_by_text(text):

  list_of_products = []
  text = text.lower()

  for product in mock_catalog:
    prod = product["title"]

    if( text in prod.lower()):
      list_of_products.append(product)

  return json.dumps(list_of_products)
#start the server
app.run(debug=True)