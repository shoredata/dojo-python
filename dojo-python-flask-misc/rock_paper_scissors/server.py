# FLASK
# ======

# Rock, Paper, Scissors
# Objectives:
# - show wins, losses, ties as persistent counters on form
#   - see session
# - 3 buttons to submit user selection via form 
# - computer selectiosn via random
# - optionally show win, loss messages instead of jsut updating score

import random
import string

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'  # Set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    initsession()    
    session['views'] += 1
    return render_template("index.html")

def initsession():
    if 'tiecount' not in session:
        session['tiecount'] = 0
        session['wincount'] = 0
        session['losscount'] = 0
        session['rocksub'] = 0
        session['papersub'] = 0
        session['scissorsub'] = 0
        session['views'] = 0

    return

@app.route('/reset', methods=['POST'])
def do_reset_session():
    print(request.form)
    print("RESET")

    initsession()    

    session['tiecount'] = 0
    session['wincount'] = 0
    session['losscount'] = 0

    session['rocksub'] = 0
    session['papersub'] = 0
    session['scissorsub'] = 0

    session['views'] = 0
    return redirect('/') # redirects back to the '/' route


# this route will handle our form submission
@app.route('/process_play/<int:userchoice>', methods=['POST'])
def create_user(userchoice):
    print(request.form)
    pcchoice = random.randint(0,2)
    print("USER:" + str(userchoice)+ ", PC:" + str(pcchoice))        

    initsession()    

    if userchoice==1:
        session['rocksub'] += 1
    elif userchoice==2:
        session['papersub'] += 1
    else:
        session['scissorsub'] += 1


    

    if userchoice==pcchoice:
        print("TIE")
        session['tiecount'] += 1 
    elif str(userchoice) + str(pcchoice) in "21,02,10":
        print("USER WINS")
        session['wincount'] += 1 
    else: 
        print("USER LOSES")
        session['losscount'] += 1 

    return redirect('/') # redirects back to the '/' route

if __name__=="__main__":
    # run our server
    app.run(debug=True) 
