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
    # A1) Run a CLASS method called getAllCUstomers().  Instaniation is not needed.
    bList=Cart.getAllCustomers()

    #Return the template index.html but pass it the list of movies
    # stored in the variable bList
    return render_template('index.html',message=bList )


#------------------------------------------------------------------------------------
# C) Create pages to INSERT records
#------------------------------------------------------------------------------------
#customer insert page
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

        # C1) Run a CLASS method called getAllCustomers().  Instaniation is not needed.
        bList=Cart.getAllCustomers()
        return render_template('customers.html',message=bList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('addcustomer.html',message='Something went wrong.')

#supplier insert page
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

#material insert page
@app.route("/addmaterial", methods=["GET","POST"]) # Decorator - Now
def addmaterial():
    if request.method == "GET":  # When you first visit the page

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllMaterials()
        sList=Cart.getAllSuppliers()
        return render_template('addmaterial.html',message=bList,suppliermessage=sList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllMaterials()
        sList=Cart.getAllSuppliers()

        # Get the value from the form object called "movtitle" (it is a textbox)
        SWPartNo = request.form.get("SWPartNo", 0)
        SupplierPartNo = request.form.get("SupplierPartNo", 0)
        SupplierID = request.form.get("SupplierID", 0)
        ProductName = request.form.get("ProductName", 0)
        Price = request.form.get("Price", 0)
        QuantityAvailable = request.form.get("QuantityAvailable", 0)

        # Run the function called saveMovieDB passing the method the title of the movie
        #   and the year the movie was release
        saveMaterialDB(SWPartNo,SupplierPartNo,SupplierID,ProductName,Price,QuantityAvailable)

        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        bList=Cart.getAllMaterials()
        return render_template('materials.html',message=bList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('addmaterial.html',message='Something went wrong.')

#place an order page 
@app.route("/placeorder", methods=["GET","POST"]) # Decorator - Now
def placeorder():
    if request.method == "GET":  # When you first visit the page

        # C1) Run a CLASS method to get all necessary details.  Instaniation is not needed.
        sList=Cart.getAllStaff()
        cList=Cart.getAllCustomers()
        pList=Cart.getAllProducts()
        oList=Cart.getAllOrders()
        mList=Cart.getAllMaterials()
        bList=Cart.getAllBOMs()
        return render_template('placeorder.html',message=sList,customermessage=cList,productmessage=pList,ordermessage=oList,bommessage=bList,materialmessage=mList)

    elif request.method == "POST": # When you fill out the form and click SUBMIT
        # C1) Run a CLASS method called getAllMovies().  Instaniation is not needed.
        sList=Cart.getAllStaff()
        cList=Cart.getAllCustomers()
        pList=Cart.getAllProducts()
        oList=Cart.getAllOrders()
        mList=Cart.getAllMaterials()
        bList=Cart.getAllBOMs()

        # Get the value from the form object (it is a drop down menu)
        EmployeeID = request.form.get("EmployeeID", 0)
        CustomerID = request.form.get("CustomerID", 0)
        ProductID1 = request.form.get("ProductID1", 0)
        Quantity1 = request.form.get("quantity1", 0)
        ProductID2 = request.form.get("ProductID2", 0)
        Quantity2 = request.form.get("quantity2", 0)
        ProductID3 = request.form.get("ProductID3", 0)
        Quantity3 = request.form.get("quantity3", 0)
        ProductID4 = request.form.get("ProductID4", 0)
        Quantity4 = request.form.get("quantity4", 0)
        ProductID5 = request.form.get("ProductID5", 0)
        Quantity5 = request.form.get("quantity5", 0)
        
        #-------------------------------------
        # 1. VERIFY IF THE PLACED ORDER DOESN'T HAVE A PRODUCT WHOSE QUANTITY IS MORE THAN 10
        #-------------------------------------
        order = {}
        if ProductID1 != "" and Quantity1 != "":
            if ProductID1 not in order.keys():
                order[ProductID1] = int(Quantity1)
            else:
                order[ProductID1] = int(order[ProductID1])+int(Quantity1)
        if ProductID2 != "" and Quantity2 != "":
            if ProductID2 not in order.keys():
                order[ProductID2] = int(Quantity2)
            else:
                order[ProductID2] = int(order[ProductID2])+int(Quantity2)
        if ProductID3 != "" and Quantity3 != "":
            if ProductID3 not in order.keys():
                order[ProductID3] = int(Quantity3)
            else:
                order[ProductID3] = int(order[ProductID3])+int(Quantity3)
        if ProductID4 != "" and Quantity4 != "":
            if ProductID4 not in order.keys():
                order[ProductID4] = int(Quantity4)
            else:
                order[ProductID4] = int(order[ProductID4])+int(Quantity4)
        if ProductID5 != "" and Quantity5 != "":
            if ProductID5 not in order.keys():
                order[ProductID5] = int(Quantity5)
            else:
                order[ProductID5] = int(order[ProductID5])+int(Quantity5)
        total = 0
        c=0
        #THROWING AN ERROR MESSAGE IF THE PLACE ORDER PAGE DID NOT HAVE ANY ORDER; THAT IS NO PRODUCT WAS PLACE 
        if len(order.keys()) == 0:
            c=1
            return render_template('placeorder.html',errormessage="You have no items added, try again!",message=sList,customermessage=cList,productmessage=pList,ordermessage=oList,bommessage=bList)
        #CHECK IF ANY ONE PRODUCT HAS MORE THAN 10 PEICES ORDERED
        for i in order.keys():
            if int(order[i]) > 10:
                c=1
                return render_template('placeorder.html',errormessage="You have more then 10 units of an item added, try again!",message=sList,customermessage=cList,productmessage=pList,ordermessage=oList)
                break
            
        #CREATING BOM FOR THE ORDER; THAT IS THE MATERIALS QUANTITY NEEDED TO PREPARE THE ORDER IS CALCULATED
        partslist = {}
        aorder = []
        #partslist example
        #{'SW01': 3.0, 'SW02': 6.0, 'OS01': 12.0, 'OS02': 3.0, 'OS03': 6.0, 'OS04': 12.0, 'OS05': 3.0, 'OS07-1': 1.5, 'OS12': 12.0}
        for j in order.keys():
            for i in bList:
                if int(j) == i['ProductID']:
                    if i['PartNo'] in partslist.keys():
                        partslist[i['PartNo']] = float(partslist[i['PartNo']]) + (float(i['Quantity'])*float(order[j]))
                    else:
                        partslist[i['PartNo']]= (float(i['Quantity'])*float(order[j]))
        #print(partslist.values()) =  [3.0,6.0,12.0]#
        #CREATE A BOM FOR THE ORDER WITH THE PRODUCT ID; THAT IS MULTIPLYING THE PRODUCT BOM WITH THE QUANTITY PLACED 
        # for i in list:
        #     print(i['Productid'])
        # l=0
        # for j in order.keys():
        #     for i in bList:
        #         if int(j) == i['ProductID']:
        #             empty=0
        #             t=0
        #             if len(aorder) != 0:
        #                 for k in aorder:
        #                     if i['ProductID'] == k['ProductID']:
        #                         l=empty
        #                         t=1
        #                         break
        #                     empty=empty+1

        #             if t==0:
        #                 l=len(aorder)
        #                 print(l)
        #                 aorder.append({})
        #                 aorder[l]['ProductID']=i['ProductID']

        #             if i['PartNo'] in aorder[l].keys():
        #                 aorder[l][i['PartNo']] = aorder[l][i['PartNo']] + (i['Quantity']*int(order[j]))
        #             else:
        #                 aorder[l][i['PartNo']]= (i['Quantity']*int(order[j]))



        #CALCULATING THE POTERNIAL ORDER THAT CAN BE PLACED WITH THE CURRENT INVENTORY
        #THIS IS CALCULATED WITH REFERENCE TO THE ORDER PLACE SO THE POTENTIAL ORDER IS EQUAL OR LESSER THAN THE ACTUAL ORDER DEPEDNING  UPON THE MATERIALS AVIALABLE
        mlistCopy=mList.copy()
        aorder={}
        clr=1
        for i in order.keys():
            pbom=getSingleBOMDictList_DB(int(i))
            aorder[i]=0
            for j in range(order[i]):
                clr=1
                for k in mlistCopy:
                    #print(k['SWPartNo'])
                    for m in pbom:
                        #print(m['PartNo'])
                        if k['SWPartNo'] == m['PartNo']:
                            diff=float(k['QuantityAvailable'])-float(m['Quantity'])
                            if diff >= 0:
                                k['QuantityAvailable'] = float(k['QuantityAvailable']) - float(m['Quantity'])
                            else:
                                clr=0
                                break
                if clr == 1:
                    aorder[i]=aorder[i]+1

        #if partslist['SWPartNo'] exists, then add, but if not set =....
        #partslist: {'SW01': 1.0, 'SW02': 2.0, 'OS01': 4.0, 'OS02': 1.0, 'OS03': 2.0, 'OS04': 4.0, 'OS05': 1.0, 'OS07-1': 0.5, 'OS12': 4.0}
        #mList: {'SWPartNo': 'SW04', 'SupplierPartNo': 'TM05', 'SupplierID': 5, 'ProductName': 'LHS Frame Small', 'Price': 3.5, 'QuantityAvailable': 1414.5}
        
        
        
        #-------------------------------------
        # 2. VERIFY IF THERE IS MATERIAL IN STOCK TO MAKE THE PRODUCTS 
        #-------------------------------------
        needmore = {}
        mList=Cart.getAllMaterials()
        for i in partslist.keys():
            for j in mList:
                if i == j["SWPartNo"] and (float(partslist[i])>float(j["QuantityAvailable"])):
                    needmore[j["SWPartNo"]] = float(partslist[i])-float(j["QuantityAvailable"])
                    c=1

        #THROWING AN ERROR MESSAGE WHEN THERE ARE NOT ENOUGH MATERIALS IN THE INVENTORY 
        if c==1:
            porder=order
            print(aorder)
            return render_template('placeorder.html',errormessage="Not enough materials in inventory, you need more:",errorpart2=needmore,errormessage2="With your material inventory, you can purchase:",errorpart3=aorder,message=sList,customermessage=cList,productmessage=pList,ordermessage=oList)
        
        #IF THERE IS ENOUGH MATERIAL IN THE INVENTORY THEN CALCULATE THE TOTAL PRICE OF THE ORDER AND PLACE THE ORDER
        if c==0:
            #[{'ProductID': 1, 'ProductName': 'Large Cart', 'Color': 'Red', 'Price': 119.99}, {'ProductID': 2, 'ProductName': 'Small Cart', 'Color': 'Blue', 'Price': 49.99}]
            for i in pList:
                for j in order.keys():
                    if int(j) == i['ProductID']:
                        total += i['Price']*float(order[j])

            Zip=getSingleDictList_DB(CustomerID)[0]["ZIP"]
            OrderID=saveOrderDB(CustomerID,EmployeeID,total,Zip)

            for i in pList:
                 for j in order.keys():
                     if int(j) == i['ProductID']:
                         saveOrderDetailDB(OrderID,int(j),float(order[j]),float(order[j])*i['Price'])
            oList=Cart.getAllOrders()
            for i in partslist.keys():
                reduceMaterialDB(float(partslist[i]),i)
        return render_template('orders.html',message=oList)

    else:
        # How could it have not been a GET or POST? I have no idea how that could have happened.
        return render_template('placeorder.html',message='Something went wrong.')

# E) Create a route to list all customers with Delete, Edit, View options
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

@app.route("/materials", methods=["GET","POST"]) # Decorator
def materialslist():
    if request.method == "GET":
        bList=Cart.getAllMaterials()
        return render_template('materials.html',message=bList)
    elif request.method == "POST":
        title = getFormVariable("title")
        bList=Cart.getAllMaterials()
        delEstimates_DB(title)

        #Reload Estimate list as a dictionary
        #DETERMINE IF THIS IS USING A CSV FILE OR DATABASE
        bDict=Cart.getAllMaterials()
        return render_template('materials.html',message=bDict )

@app.route("/orders", methods=["GET","POST"]) # Decorator
def orderslist():
    if request.method == "GET":
        bList=Cart.getAllOrders()
        return render_template('orders.html',message=bList)
    elif request.method == "POST":
        title = getIntegerFormVariable("title")
        bList=Cart.getAllOrders()
        delEstimates_DB(title)

        #Reload Estimate list as a dictionary
        #DETERMINE IF THIS IS USING A CSV FILE OR DATABASE
        bDict=Cart.getAllOrders()
        return render_template('orders.html',message=bDict )

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

@app.route("/EditMaterial/<title>", methods=['POST', 'GET'])
def EditMaterialFUNCTION(title):
    if request.method == "GET":
        # GET THE MOVIE FOR THE ID
        mSingleDict=getSingleMaterialDictList_DB(title)
        # PASS THE SINGLE MOVIE TO THE edit.html PAGE
        return render_template('updatematerial.html',message=mSingleDict )

# @app.route("/EditBOM/<title>", methods=['POST', 'GET'])
# def EditBOMFUNCTION(title):
#     if request.method == "GET":
#         # GET THE MOVIE FOR THE ID
#         mSingleDict=getSingleBOMDictList_DB(title)
#         # PASS THE SINGLE MOVIE TO THE edit.html PAGE
#         return render_template('updatebom.html',message=mSingleDict )

@app.route("/EditSupplier/<title>", methods=['POST', 'GET'])
def EditSupplierFUNCTION(title):
    if request.method == "GET":
        # GET THE MOVIE FOR THE ID
        mSingleDict=getSingleSupplierDictList_DB(title)
        # PASS THE SINGLE MOVIE TO THE edit.html PAGE
        return render_template('updatesupplier.html',message=mSingleDict )

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

@app.route("/EditMaterial", methods=["GET","POST"]) # Decorator - Now
def EditMaterialSave():
    # GET THE VALUES FROM THE FORM - USE THE FUNCTIONS AT THE BOTTOM OF THIS
    # CODE PAGE TO HELP YOU GET THE VALUSE
    SWPartNo = getFormVariable("SWPartNo")
    SupplierPartNo = getFormVariable("SupplierPartNo")
    SupplierID = getIntegerFormVariable("SupplierID")
    ProductName = getFormVariable("ProductName")
    Price = getFormVariable("Price")
    QuantityAvailable = getFloatFormVariable("QuantityAvailable")


    # CALL THE FUNCTION updateMovieDB and pass the new values
    xID = updateMaterialDB(
            SupplierPartNo,SupplierID,ProductName,Price,QuantityAvailable,SWPartNo)
    # Retrive the new values from the database and ...
    bList=Cart.getAllMaterials()
    return render_template('materials.html',message=bList)

@app.route("/EditSupplier", methods=["GET","POST"]) # Decorator - Now
def EditSupplierSave():
    # GET THE VALUES FROM THE FORM - USE THE FUNCTIONS AT THE BOTTOM OF THIS
    # CODE PAGE TO HELP YOU GET THE VALUSE
    SupplierID = getIntegerFormVariable("SupplierID")
    ZIP = getFormVariable("ZIP")
    Telephone = getFormVariable("Telephone")
    Email = getFormVariable("Email")

    # CALL THE FUNCTION updateMovieDB and pass the new values
    xID = updateSupplierDB(
            ZIP,Telephone,Email,SupplierID)
    # Retrive the new values from the database and ...
    bList=Cart.getAllSuppliers()
    return render_template('suppliers.html',message=bList)

# @app.route("/EditBOM", methods=["GET","POST"]) # Decorator - Now
# def EditBOMSave():
#     # GET THE VALUES FROM THE FORM - USE THE FUNCTIONS AT THE BOTTOM OF THIS
#     # CODE PAGE TO HELP YOU GET THE VALUSE
#     SupplierID = getIntegerFormVariable("SupplierID")
#     ZIP = getFormVariable("ZIP")
#     Telephone = getFormVariable("Telephone")
#     Email = getFormVariable("Email")

#     # CALL THE FUNCTION updateMovieDB and pass the new values
#     xID = updateSupplierDB(
#             ZIP,Telephone,Email,SupplierID)
#     # Retrive the new values from the database and ...
#     bList=Cart.getAllSuppliers()
#     return render_template('suppliers.html',message=bList)

#------------------------------------------------------------------------------------
#E) Create a route to DISPLAY a single movie
#------------------------------------------------------------------------------------
@app.route("/orderdetails/<title>", methods=['POST', 'GET'])
def DisplayFUNCTION(title):
    # GET THE MOVIE FOR THE ID
    mSingleDict=getSingleOrderDictList_DB(title)
    Date=getSingleODictList_DB(title)[0]["Date"]
    # PASS THE SINGLE MOVIE TO THE edit.html PAGE
    return render_template('orderdetails.html',message=mSingleDict,D=Date)

@app.route("/bomdetails/<title>", methods=['POST', 'GET'])
def DisplayBOMFUNCTION(title):
    # GET THE MOVIE FOR THE ID
    mSingleDict=getSingleBOMDictList_DB(title)
    # PASS THE SINGLE MOVIE TO THE edit.html PAGE
    return render_template('bomdetails.html',message=mSingleDict)


#------------------------------------------------------------------------------------
#E) Create a route to DELETE a single row
#------------------------------------------------------------------------------------
@app.route("/deleteFromList/<title>", methods=['POST', 'DELETE', 'GET'])
def deleteFromList(title):
    # CALL THE DELMOVIES_DB function passing it the ID of the movie
    genDelete_DB("Customers","CustomerID",title)
    # Once the movie is deleted, get the new list of movies and ...
    bDict=Cart.getAllCustomers()
    # display it on the movielist page
    return render_template('customers.html',message=bDict )

@app.route("/deleteSupplierFromList/<title>", methods=['POST', 'DELETE', 'GET'])
def deleteSupplierFromList(title):
    # CALL THE DELMOVIES_DB function passing it the ID of the movie
    genDelete_DB("Suppliers","SupplierID",title)
    # Once the movie is deleted, get the new list of movies and ...
    bDict=Cart.getAllSuppliers()
    # display it on the movielist page
    return render_template('suppliers.html',message=bDict )

@app.route("/deleteMaterialFromList/<title>", methods=['POST', 'DELETE', 'GET'])
def deleteMaterialFromList(title):
    # CALL THE DELMOVIES_DB function passing it the ID of the movie
    genDelete_DB("Materials","SWPartNo",title)
    # Once the movie is deleted, get the new list of movies and ...
    bDict=Cart.getAllMaterials()
    # display it on the movielist page
    return render_template('materials.html',message=bDict )

# 1. FUNCTION TO HELP GET VARIABLES FROM FORMS
#---------------------------
def getFormVariable(variableName):
    return request.form.get(variableName, 0)

def getIntegerFormVariable(variableName):
    return int(request.form.get(variableName, 0))

def getFloatFormVariable(variableName):
    return float(request.form.get(variableName, 0))


if __name__ == '__main__':
    app.run(debug=True)
