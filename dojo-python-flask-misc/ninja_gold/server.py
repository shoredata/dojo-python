import datetime
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = "789yh9"

def initsession():
    if 'ninja' not in session:
        session['ninja'] = ""
        session['bank'] = 0
        session['action'] = ["<div style='color: black;'>" + "Initialized " + str(datetime.datetime.now()) + "</div>"]
    return

def clearsession():
    session.clear()
    return

def addaction(action):
    initsession()
    session['action'].insert(0, action)      
    print(action)
    return 

@app.route('/')         
def index():
    print("-- ROOT --" + str(datetime.datetime.now()))
    initsession()
    return render_template("index.html")

@app.route('/reset', methods=['POST'])         
def do_reset():
    print("-- RESET --" + str(datetime.datetime.now()))
    clearsession()
    return redirect("/")


@app.route('/process', methods=['POST'])         
def checkout():
    print("-- PROCESS --" + str(datetime.datetime.now()))
    initsession()
    # print(request.form)    
    # farm: +10-20
    # cave: +5-10
    # house: +2-5
    # casino: +/-0-50
    bounds ={
        'farm': {'min':10, 'max':20} ,
        'cave': {'min':5, 'max':10} ,
        'house': {'min':2, 'max':5} ,
        'casino': {'min':-50, 'max':50}
    }
    bldg = request.form['building']
    min = bounds[bldg]['min']
    max = bounds[bldg]['max']
    amount = random.randint(min,max)
    session['bank'] += amount

    if amount>0:
        addaction("<div style='color: green;'>" + bldg + " ALL RIGHT YOU WON " + str(amount) + " ! ! (" + str(datetime.datetime.now()) + ")</div>")
    else:
        addaction("<div style='color: red;'>" + bldg + " TOO BAD YOU LOST " + str(amount*-1) + " :( :( :(  (" + str(datetime.datetime.now()) + ")</div>")

    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True)    







# output:

