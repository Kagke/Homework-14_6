from flask import render_template , request , redirect
from app import app
from models.event import *
from models.event_planer import *


@app.route("/events" , methods=["GET"])
def index():
    return render_template("base.html", title="Events", events=events )



@app.route('/events', methods=['POST'])
def add_events():
    event_title = request.form["name"] 
    event_date = request.form["date"]
    print(event_date)
    split_date = event_date.split("-")
    print(split_date)
    date=datetime.date(int(split_date[0]),int(split_date[1]),int(split_date[2]))
    event_num_of_guest = request.form["num_of_guest"]
    event_room_location = request.form["room_location"]
    event_description=request.form["description"]
    event_recurring=request.form["recurring"]
    new_event = Events (event_title ,date, event_num_of_guest ,event_room_location ,event_description,event_recurring)
    add_event(new_event)
    return redirect("/events")

@app.route("/events/delete/<index>" , methods = ["POST"])
def remove(index):
     removing_event = events[int(index)]
     remove_event(removing_event)
     return redirect("/events")
     
   

     

