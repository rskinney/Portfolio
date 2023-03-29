###############################################################################
#                         IMPORT REQUIRED LIBRARIES/MODULES
###############################################################################
# 1. The FLASK framework (the webserver)
from flask import Flask

from flask import redirect, url_for #The FLASK framework (the webserver)

# 2. For opening and read the HTML file and showing them as the webpage
from flask import render_template

# 3. From the flask library import the request class.
# Allows us to get information from the website URL
from flask import request

# 4. From the objects.py containing our classes for this application, only import the Movie class
from objects import Cart

# 5. Import the sqlite library
# import sqlite3

# 6. Instantiate the Flask() class and called it app
app=Flask(__name__)

# 7. Import your database functions from a separte file called database.py
from database import *


###############################################################################
#                         CREATE YOUR WEBPAGE ROUTES
###############################################################################

# -----------------------------------------------------------------------------
# A) Create your home page.  Let's call the page "index"
# -----------------------------------------------------------------------------

#   Start with a decorator with no name. That way when they only type in your server's name
#   It will got to this page
@app.route("/")

#   Let's also add the name "index" since that is a common name for a website home page
@app.route("/index")    # Decorator - Now

#   Define what should happen when visiting this page by using a function called index()
def index():
    # A1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
    bList=Cart.getAllCustomers()

    #Return the template index.html but pass it the list of movies
    # stored in the variable bList
    return render_template('index.html',message=bList )



# -----------------------------------------------------------------------------
# B) Create a page to DELETE records
#------------------------------------------------------------------------------

# Create a decorator with the route/path "delete".
# IMPORTANT: THIS IS A FORM!!!
# Allowable Actions:
#   GET:  This is when you first come to the page
#   POST: This is when you SUBMIT the information that you filled out in the form
@app.route("/delete", methods=["GET","POST"]) # Decorator - Now

#   Define what should happen when visiting this page by using a function called delete
def delete():
    if request.method == "GET":  # When you first visit the page

        # B1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCarts()
        return render_template('delete.html',message=bList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # Get the value from the form object called "movtitle" (it is a textbox)
        Carttitle = request.form.get("title", 0)

        # B1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCarts()
        delCarts_Title_DB(Carttitle)

        # B1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCarts()

        #Return the template index.html but pass it the list of movies
        # stored in the variable mList
        return render_template('delete.html',message=bList )

    else:
        # How could it have not been a GET or POST? Hmm. Should have been one of them.
        return render_template('delete.html',message="Something did not work.")


#------------------------------------------------------------------------------------
# C) Create a page to INSERT records
#------------------------------------------------------------------------------------

@app.route("/addcustomer", methods=["GET","POST"]) # Decorator - Now
def addcustomer():
    if request.method == "GET":  # When you first visit the page

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCustomers()
        return render_template('addcustomer.html',message=bList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCustomers()

        # Get the value from the form object called "movtitle" (it is a textbox)
        name = request.form.get("name", 0)
        zip = request.form.get("ZIP", 0)
        telephone = request.form.get("telephone", 0)
        email = request.form.get("email", 0)
        category = request.form.get("category", 0)

        # Run the function called saveMovieDB passing the method the title of the movie
        #   and the year the movie was release
        saveCustomerDB(name, zip, telephone, email, category)

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllCustomers()
        return render_template('customers.html',message=bList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('addcustomer.html',message='Something went wrong.')

@app.route("/addsupplier", methods=["GET","POST"]) # Decorator - Now
def addsupplier():
    if request.method == "GET":  # When you first visit the page

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllSuppliers()
        return render_template('addsupplier.html',message=bList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllSuppliers()

        # Get the value from the form object called "movtitle" (it is a textbox)
        name = request.form.get("name", 0)
        zip = request.form.get("ZIP", 0)
        telephone = request.form.get("telephone", 0)
        email = request.form.get("email", 0)

        # Run the function called saveMovieDB passing the method the title of the movie
        #   and the year the movie was release
        saveSupplierDB(name, zip, telephone, email)

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllSuppliers()
        return render_template('suppliers.html',message=bList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('addsupplier.html',message='Something went wrong.')


@app.route("/placeorder", methods=["GET","POST"]) # Decorator - Now
def placeorder():
    if request.method == "GET":  # When you first visit the page

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        sList=Cart.getAllStaff()
        cList=Cart.getAllCustomers()
        return render_template('placeorder.html',message=sList,customermessage=cList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllStaff()

        # Get the value from the form object called "movtitle" (it is a textbox)
        EmployeeID = request.form.get("EmployeeID", 0)

        # Run the function called saveMovieDB passing the method the title of the movie
        #   and the year the movie was release
        #saveCustomerDB(name, zip, telephone, email, category)

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllStaff()
        return render_template('customers.html',message=bList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('placeorder.html',message='Something went wrong.')

# E) Create a route to list all movies with Delete, Edit, View options
#------------------------------------------------------------------------------------
@app.route("/customers", methods=["GET"]) # Decorator
def customerslist():
    if request.method == "GET":
        bList=Cart.getAllCustomers()
        return render_template('customers.html',message=bList)

@app.route("/products", methods=["GET","POST"]) # Decorator
def productslist():
    if request.method == "GET":
        bList=Cart.getAllProducts()
        return render_template('products.html',message=bList)
    elif request.method == "POST":
        title = getIntegerFormVariable("title")
        bList=Cart.getAllCarts()
        delEstimates_DB(title)

        #Reload Estimate list as a dictionary
        #DETERMINE IF THIS IS USING A CSV FILE OR DATABASE
        bDict=Cart.getAllCarts()
        return render_template('CartList.html',message=bDict )

@app.route("/suppliers", methods=["GET","POST"]) # Decorator
def supplierslist():
    if request.method == "GET":
        bList=Cart.getAllSuppliers()
        return render_template('suppliers.html',message=bList)
    elif request.method == "POST":
        title = getIntegerFormVariable("title")
        bList=Cart.getAllCarts()
        delEstimates_DB(title)

        #Reload Estimate list as a dictionary
        #DETERMINE IF THIS IS USING A CSV FILE OR DATABASE
        bDict=Cart.getAllCarts()
        return render_template('CartList.html',message=bDict )

#------------------------------------------------------------------------------------
#E) Create a route to EDIT an individual movie
#------------------------------------------------------------------------------------
# NOTE**** THIS EDIT HAS <int:ID> added to it
@app.route("/Edit/<title>", methods=['POST', 'GET'])
def EditFUNCTION(title):
    if request.method == "GET":
        # GET THE MOVIE FOR THE ID
        mSingleDict=getSingleDictList_DB(title)
        # PASS THE SINGLE MOVIE TO THE edit.html PAGE
        return render_template('updatecustomer.html',message=mSingleDict )

#------------------------------------------------------------------------------------
#E) Create a route to SAVE an individual movie after EDIT
#------------------------------------------------------------------------------------
# NOTE**** THIS EDIT DOES NOT HAVE THE <int:ID> added to it
@app.route("/Edit", methods=["GET","POST"]) # Decorator - Now
def EditSave():
    # GET THE VALUES FROM THE FORM - USE THE FUNCTIONS AT THE BOTTOM OF THIS
    # CODE PAGE TO HELP YOU GET THE VALUSE
    customerID = getIntegerFormVariable("CustomerID")
    name = getFormVariable("Name")
    zip = getFormVariable("ZIP")
    telephone = getFormVariable("Telephone")
    email = getFormVariable("Email")
    category = getFormVariable("Category")


    # CALL THE FUNCTION updateMovieDB and pass the new values
    xID = updateCustomerDB(
            customerID, zip, telephone, email, category)
    # Retrive the new values from the database and ...
    bList=Cart.getAllCustomers()
    return render_template('customers.html',message=bList)

#------------------------------------------------------------------------------------
#E) Create a route to DISPLAY a single movie
#------------------------------------------------------------------------------------
@app.route("/Display/<title>", methods=['POST', 'GET'])
def DisplayFUNCTION(title):
    # GET THE MOVIE FOR THE ID
    mSingleDict=getSingleDictList_DB(title)
    print(title)
    # PASS THE SINGLE MOVIE TO THE edit.html PAGE
    return render_template('display.html',message=mSingleDict )


#------------------------------------------------------------------------------------
#E) Create a route to DELETE a single movie
#------------------------------------------------------------------------------------
@app.route("/deleteFromList/<title>", methods=['POST', 'DELETE', 'GET'])
def deleteFromList(title):
    # CALL THE DELMOVIES_DB function passing it the ID of the movie
    delCustomer_DB(title)
    # Once the movie is deleted, get the new list of movies and ...
    bDict=Cart.getAllCustomers()
    # display it on the movielist page
    return render_template('customers.html',message=bDict )

@app.route("/deleteSupplierFromList/<title>", methods=['POST', 'DELETE', 'GET'])
def deleteSupplierFromList(title):
    # CALL THE DELMOVIES_DB function passing it the ID of the movie
    delSupplier_DB(title)
    # Once the movie is deleted, get the new list of movies and ...
    bDict=Cart.getAllSuppliers()
    # display it on the movielist page
    return render_template('suppliers.html',message=bDict )

# 1. FUNCTION TO HELP GET VARIABLES FROM FORMS
#---------------------------
def getFormVariable(variableName):
    return request.form.get(variableName, 0)

def getIntegerFormVariable(variableName):
    return int(request.form.get(variableName, 0))



if __name__ == '__main__':
    app.run(debug=True)
