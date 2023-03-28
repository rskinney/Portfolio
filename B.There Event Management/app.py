from os import name
from flask import Flask, render_template, redirect, url_for, request
from os.path import exists

app = Flask(__name__)

#very simple error checker, takes in user inputs and then checks the length and if they exist.
def eventcheck(name,date,host,description):
    error = ""
    msg=[]
    if not name:
        msg.append("Name is missing!")
    if len(name) > 25:
        msg.append("Name is too long!")
    if not date:
        msg.append("Date is missing!")
    if len(date) > 12:
        msg.append("Date is the incorrect length!")
    if not host:
        msg.append("Host is missing!")
    if len(host) > 20:
        msg.append("Host name is too long!")
    if not description:
        msg.append("Description is missing!")
    if len(description) > 255:
        msg.append("Description is too long!")
    #prints out message only if there's an error
    if len(msg) > 0:
        error=" \n".join(msg)
    return error

#same one as before, just different variables
def attendeecheck(name,email,comment):
    error = ""
    msg=[]
    if not name:
        msg.append("Name is missing!")
    if len(name) > 25:
        msg.append("Name is too long!")
    if not email:
        msg.append("Email is missing!")
    if len(email) > 100:
        msg.append("Email is too long!")
    if not comment:
        msg.append("Comment is missing!")
    if len(comment) > 255:
        msg.append("Comment is too long!")
    if len(msg) > 0:
        error=" \n".join(msg)
    return error

#Connecting to my database via PyMySQL, using a config.py file
app.config.from_pyfile(app.root_path + '/config_defaults.py')
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')

import database

#Simply will be returning the index.html whenever we access it, nothing complicated on there.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events/')
@app.route('/events/<event_id>')

#For the events page, we are going to use the get_events() function from database to return a list of dicts with all the events in it.
def events(event_id=None):
    events = database.get_events()
    #if there is a singular event being put in here, we know to return the event page with both the content from that event as well as
    #the attendees that will be at that event.
    if event_id:
        attendees = database.get_attendees(event_id)
        event = database.get_event(event_id)
        #passing these things through so the website knows what information to show.
        return render_template('event.html', event=event, attendees=attendees)
    else:
        return render_template('events.html', events=events)

@app.route('/events/create', methods=['GET', 'POST'])

#This function will be used to add directly to a particular event's table in the database.
def create():
    if request.method == 'POST':
        #using form requests to get all of this information before passing it straight through to the add_event() function.
        name = request.form['name']
        date = request.form['date']
        host = request.form['host']
        description = request.form['description']
        error = eventcheck(name,date,host,description)
        if error:
            return render_template("event_form.html", error=error, name=name, date=date, host=host, description=description)
        database.add_event(name,date,host,description)
        #once that's complete, we redirect to the events route to see it added to the list.
        return redirect(url_for('events'))
    else:
        #if it doesn't work, we keep it on the event_form.html page so the user can try their changes again
        return render_template('event_form.html')


    
@app.route('/events/<event_id>/edit', methods=['GET', 'POST'])

def edit(event_id=None):
    #This is very similar to the last function, just takes in an event_id so that the function knows what event it will be editing
    event = database.get_event(event_id)
    attendees = database.get_attendees(event_id)
    if request.method == 'POST':
        date = request.form['date']
        name = request.form['name']
        host = request.form['host']
        description = request.form['description']
        error = eventcheck(name,date,host,description)
        if error:
            return render_template("event_form.html", event=event, error=error, name=name, date=date, host=host, description=description)
        #using the edit_event() function from database
        database.edit_event(event_id,name,date,host,description)
        event = database.get_event(event_id) #Getting this again in case the user updates, will want to see the changes immediately
        #once done with the edit, it will show the user that newly edited page
        return render_template('event.html', event=event, attendees=attendees)
    else:
        return render_template('event_form.html', event=event)

@app.route('/events/<event_id>/delete', methods=['GET', 'POST'])

#This allows the user to delete events from the database
def delete(event_id=None):
    #using get_event() to display information on the delete_form.html
    event = database.get_event(event_id)
    if request.method == 'POST':
        #very simple, just uses the delete_event() function with the event_id as a parameter to remove it entirely
        database.delete_event(event_id)
        #once this is complete, it will return to the events page to show that it has been removed.
        return redirect(url_for('events'))
    else:
        return render_template('delete_form.html', event=event)

@app.route('/events/<event_id>/attendees/add', methods=['GET', 'POST'])

def add_attendee(event_id=None):
    #very similar to the add event function
    event = database.get_event(event_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']
        error = attendeecheck(name,email,comment)
        if error:
            return render_template("attendee_form.html", error=error, event=event, name=name, email=email, comment=comment)
        #uses the form to create an attendee in database's add_attendee() function based on the event_id that the user is currently on, tying the attendee to a particular event as a foreign key
        database.add_attendee(event_id,name,email,comment)
        #once it's done, it'll redirect to the particular event where the attendee was added
        return redirect(url_for('events', event_id=event_id))
    else:
        #if it fails, it will return to the page where they will be typing attendee info
        return render_template('attendee_form.html', event=event)

@app.route('/events/<event_id>/attendees/<attendee_id>/edit', methods=['GET','POST'])

def edit_attendee(attendee_id,event_id):
    #this acquires the event dictionary as well as the attendee dictionary for the particular page and event we're looking for
    event = database.get_event(event_id)
    attendee = database.get_attendee(attendee_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']
        error = attendeecheck(name,email,comment)
        if error:
            return render_template("attendee_form.html", error=error, event=event, attendee=attendee, name=name, email=email, comment=comment)
        #using this info, we use the edit_attendee() function in the database.py to make the changes that the user types in the form we're requesting
        database.edit_attendee(attendee_id,event_id,name,email,comment)
        #once done, we'll want to return to the page that the user was originally on.
        return redirect(url_for('events',event_id=event_id))
    else:
        return render_template('attendee_form.html', attendee=attendee, event=event)

@app.route('/events/<event_id>/attendees/<attendee_id>/delete', methods=['GET', 'POST'])

def del_attendee(attendee_id,event_id):
    #similarly to the last one, takes in the attendee_id and event_id in order to find a specific attendee. Uses the del_attendee() function with that specific information.
    database.del_attendee(attendee_id,event_id)
    #once done, redirects to the specific event page we're looking for
    return redirect(url_for('events',event_id=event_id))


