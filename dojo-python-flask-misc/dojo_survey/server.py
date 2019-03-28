# FLASK
# ======

# Form, Post, and Redirect
# Objectives:
# How do we use HTML forms to send data to the server?
# A: The action attribute
# This attribute defines where the data gets sent. Its value must be a valid URL. If this attribute isn't provided, the data will be sent to the URL of the page containing the form.
# What does the action attribute in an HTML form mean?
# A: The action attribute specifies where to send the form-data when a form is submitted.
# What does the method attribute in an HTML form mean?
# What change do we have to make in our Flask server to indicate that a route may accept POST requests?
# How can we access the data from the HTML form when it gets to the server?
# What does it mean to redirect in the context of routing?

import re
import datetime

from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

app.secret_key = "adsf43t&*^dsdsf_?^&*()"

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')


def test_password(passin):
    passw = str(passin)
    x = [True,""]
    while x[0]:  
        if not re.search("[a-z]",passw):
            x[1] = "No lowercase character found"
            break
        elif not re.search("[0-9]",passw):
            x[1] = "No numeric found"
            break
        elif not re.search("[A-Z]",passw):
            x[1] = "No uppercase found"
            break
        elif re.search("\s",passw):
            x[1] = "Invalid character(s) found"
            break
        else:
            x[0]=False
            break
    x[0] = not x[0]
    if not x[0]:
        print(x[1])
    return x




# our index route will handle rendering our form
# @app.route('/')
# def index():
#     return render_template("index.html")
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if (path==""):
        print("-- index: blank path: default --")
        return render_template("index.html")
    else:
        print("-- index: unexpected path: {" + path + "} --> display 404 --")
        return render_template("index.html")

def initsession():
    session.clear()
    return

def savesession(key,value,type0str1int=0):
    if type0str1int == 0:
        session[key] = str(value)
    else:
        session[key] = int(value)
    return 

def isDateValid(sdate):
    dateValid = False
    try:
        newDate = datetime.datetime(sdate)
        dateValid = True
    except ValueError:
        dateValid = False
    return dateValid




# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")

    session.pop('_flashes', None)

    savesession('namefirst',request.form['namefirst'])
    savesession('namelast',request.form['namelast'])
    savesession('email',request.form['email'])
    savesession('dob',request.form['dob'])
    # savesession('location',request.form['location'])
    # savesession('language',request.form['language'])

    # print(request.form)
    for x in request.form:
        print(x+":",request.form[x])

    if 'Reset' in request.form:
        if request.form['Reset']=='Reset':
            print("User Reset")
            session.clear()
            return redirect('/')
    

    # name = request.form['name']

    # ###### VALIDATION ################################
    bsuccess = True

    ### EMAIL #############################################
    if 'email' in request.form:
        if len(request.form['email']) < 1:
            flash("ERROR: Email must not be blank",'email')
            bsuccess = False
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("ERROR: Invalid Email Address",'email')
            bsuccess = False
    else:
        flash("ERROR: Email must not be blank",'email')
        bsuccess = False

    ### DOB #############################################
    if 'dob' in request.form:
        if len(request.form['dob']) < 1:
            flash("ERROR: Date of Birth must not be blank",'dob')
            bsuccess = False
        elif not isDateValid(request.form['dob']):
            flash("ERROR: Invalid Date of Birth",'dob')
            bsuccess = False
    else:
        flash("ERROR: Date of Birth must not be blank",'dob')
        bsuccess = False

    ### FIRST NAME #############################################
    if 'namefirst' in request.form:
        if len(request.form['namefirst']) < 1:
            flash("ERROR: First Name must not be blank",'namefirst')
            bsuccess = False
        elif not NAME_REGEX.match(request.form['namefirst']):
            flash("ERROR: Invalid First Name - Alpha Characters Only",'namefirst')
            bsuccess = False
    else:
        flash("ERROR: First Name must not be blank",'namefirst')
        bsuccess = False

    ### LAST NAME #############################################
    if 'namelast' in request.form:
        if len(request.form['namelast']) < 1:
            flash("ERROR: Last Name must not be blank",'namelast')
            bsuccess = False
        elif not NAME_REGEX.match(request.form['namelast']):
            flash("ERROR: Invalid Last Name - Alpha Characters Only",'namelast')
            bsuccess = False
    else:
        flash("ERROR: Last Name must not be blank",'namelast')
        bsuccess = False

    ### PASSWORD #############################################
    if 'password' in request.form:
        if len(request.form['password']) < 1:
            flash("ERROR: Password must not be blank",'password')
            bsuccess = False
        else:
            ### CONFIRM PASSWORD #############################################
            if 'passwordconfirm' in request.form:
                if len(request.form['passwordconfirm']) < 1:
                    flash("ERROR: Confirm Password must not be blank",'passwordconfirm')
                    bsuccess = False
                else:
                    if request.form['password'] != request.form['passwordconfirm']:
                        flash("ERROR: Passwords do not match",'password')
                        flash("ERROR: Passwords do not match",'passwordconfirm')
                        bsuccess = False
                    else:
                        ### PASSWORD REGEX #############################################
                        if not PASSWORD_REGEX.match(request.form['password']):
                            flash("ERROR: Invalid Character in Password!",'password')
                            flash("ERROR: Invalid Character in Password!",'passwordconfirm')
                            bsuccess = False
                        else:
                            testpw =  test_password(request.form['password'])
                            if not testpw[0]:
                                flash("ERROR: " + testpw[1],'password')
                                flash("ERROR: " + testpw[1],'passwordconfirm')
                                bsuccess = False
                            else:
                                ### PASSWORDS MATCH AND ARE VALID #############################################
                                flash("SUCCESS", "all")

            else:
                flash("ERROR: Confirm Password must not be blank",'passwordconfirm')
                bsuccess = False
    else:
        flash("ERROR: Password must not be blank",'password')
        bsuccess = False




    # ### COMMENT #############################################
    # if 'comment' in request.form:
    #     if len(request.form['comment']) > 120:
    #         flash("ERROR: Comment must be less than 120 characers",'comment')
    #         bsuccess = False



    return redirect('/')



if __name__=="__main__":
    # run our server
    app.run(debug=True) 
