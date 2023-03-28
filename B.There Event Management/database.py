import pymysql
from app import app

#creating a function that checks the app.config for our login to the IU database
def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)

#this function accesses the database and acquires every event, putting them in a list of dictionaries
def get_events():
    sql = "select * from events order by date,name"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

#this will take the user's input and add another event to the events table
def add_event(name,date,host,description):
    #to make life easier, we use %s
    sql = "insert into events (name,date,host,description) values (%s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            #executing these values
            cursor.execute(sql, (name,date,host,description))
        #commiting these to the db
        conn.commit()

#very similar to the get_events function, this one just gets all the info from one event based on the event_id
def get_event(event_id):
    sql = "select * from events where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
            #fetchone() just returns one value rather than a list of dictionaries, just making this a one dict return
            return cursor.fetchone()

#this function will allow the user to edit every value in a particular event
def edit_event(event_id,name,date,host,description):
    sql = "UPDATE events SET name = %s, date = %s, host = %s, description = %s WHERE id= %s"
    #this query will change all of the values the user desires based on the event_id, ensuring that's the only one that gets changed
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            #executing this query
            cursor.execute(sql, (name,date,host,description,event_id))
        #committing these changes to the db
        conn.commit()

#this allows us to delete a particular event from the database
def delete_event(event_id):
    #deleting attendees first to not mess with foreign keys
    sql = "delete from attendees where event_id = %s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
        #once again, executing and committing these changes
        conn.commit()
    #now the event_id to ensure that the correct event actually gets deleted
    sql = "delete from events where id = %s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
        #once again, executing and committing these changes
        conn.commit()
        
#these next several are very similar to the events respective functions
def get_attendees(event_id):
    #selecting every attendee in the list of attendees, this time it's ensuring that they're in the particular event we're viewing at the time though.
    sql = "SELECT * FROM attendees WHERE event_id = %s ORDER BY name"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
        #this time we're using cursor.fetchall() to return a list of dictionaries that we can traverse
        return cursor.fetchall()

def get_attendee(attendee_id):
    #just acquires one attendee based on the attendee_id
    sql = "select * from attendees where id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (attendee_id))
        #uses fetchone() to ensure that it just returns the one attendee that we're looking for
        return cursor.fetchone()

def add_attendee(event_id,name,email,comment):
    #this function allows the user to add attendees to their list, very barebones on here but better utilized on the app.py page, uses a combination of information sources
    sql = "insert into attendees(event_id,name,email,comment) values (%s,%s,%s,%s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id,name,email,comment))
        #committing these changes to the db
        conn.commit()

def edit_attendee(id,event_id,name,email,comment):
    #here we use an update query to change an attendee's information. Just in case we add functionality for a user to use the same ID on multiple events, we ensure that it only removes the user if they also match the particular event page we're on.
    sql = "update attendees set name = %s, email = %s, comment = %s where id = %s and event_id= %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name,email,comment,id,event_id))
        #committing these changes to the db
        conn.commit()

def del_attendee(attendee_id,event_id):
    #here we're once again considering the possibility of a repeat attendee_id, but we're deleting users from the database using a delete from query
    sql = "delete from attendees where id = %s and event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (attendee_id, event_id))
        #using execute and commit to finalize these changes to the database.
        conn.commit()




