import datetime
import re

from flask import Flask, render_template, request, redirect, session, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconn import connectToMySQL

app = Flask(__name__)
app.secret_key = "&Yasdfadsfasd89769fadsIUHI*H";
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
dbname='friendsdb'
mysql = connectToMySQL(dbname)

def savesession(key,value,type0str1int=0):
    if type0str1int == 0:
        session[key] = str(value)
    else:
        session[key] = int(value)
    return 

def initsession():
    if 'namefirst' not in session:
        session['namefirst'] = ''
        session['namelast'] = ''
        session['occupation'] = ''
    return

def clearsession():
    session.clear()
    return


def does_form_data_exist():
    exists = False
    tablename = 'friends'
    # in this simple exercise all 3 fields must exist
    myquery = "SELECT * FROM " + tablename + " WHERE "
    myquery += " first_name = '" + request.form['namefirst'] + "' AND "
    myquery += " last_name = '" + request.form['namelast'] + "' AND "
    myquery += " occupation = '" + request.form['occupation'] + "' "
    myquery += " ;"
    # myquery = "SELECT * FROM friends WHERE  first_name = 'adsfadsfsdf' AND last_name = 'asdfadsfadsfdasasdfadsfasdfasdfasdf' AND occupation = 'asdfadsfadsfasdfasdfads';"
    print(myquery)
    myresults = mysql.query_db(myquery)
    print("mysql >> " + dbname + "::" + tablename + "::"+myquery)
    for i in myresults: 
        print(i)
        exists = True
    return exists

@app.route('/')
def index():
    initsession()
    tablename = 'friends'
    allquery = "SELECT * FROM " + tablename + ";"
    allresults = mysql.query_db(allquery)
    print(allquery)
    print("mysql >> " + dbname + "::" + tablename + "::"+allquery)
    # for i in allresults: 
    #     print(i)
    #     for k in i:
    #         print('\t',k,i[k])  

    return render_template('index.html', friends = allresults)


@app.route('/create_friend', methods=['POST'])
def create():
    print("Got Post Info")
    session.pop('_flashes', None)

    print('\nsession:')
    for x in session:
        print(x+":",request.form[x])

    savesession('namefirst',request.form['namefirst'])
    savesession('namelast',request.form['namelast'])
    savesession('occupation',request.form['occupation'])
    print("session saved ..")

    print("\nform:")
    for x in request.form:
        print(x+":",request.form[x])
    print("data printed ..")

    if 'Reset' in request.form:
        if request.form['Reset']=='Reset':
            print("User Reset")
            clearsession()
            return redirect('/')

    # ###### VALIDATION ################################
    bsuccess = True

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

    ### OCCUPATION #############################################
    if 'occupation' in request.form:
        if len(request.form['occupation']) < 1:
            flash("ERROR: Occupation must not be blank",'occupation')
            bsuccess = False
        elif not NAME_REGEX.match(request.form['occupation']):
            flash("ERROR: Invalid Occupation - Alpha Characters Only",'occupation')
            bsuccess = False
    else:
        flash("ERROR: Occupation must not be blank",'occupation')
        bsuccess = False

    if bsuccess:
        flash("All Fields Valid ....",'all')

        if does_form_data_exist():
            flash("Error: User already exists!!", "all")
        else :

            myquery = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(occupation)s, now(), now() );"
            print(myquery)
            mydata = {
                    'first_name': request.form['namefirst'],
                    'last_name':  request.form['namelast'],
                    'occupation': request.form['occupation'],
                    'created_at': str(datetime.datetime.now()),
                    'updated_at': str(datetime.datetime.now())
            }
            print(mydata)

            insert_id = mysql.query_db(myquery, mydata)
            print("Inserted: " + str(insert_id))
            clearsession()
            flash("Friend Added!",'all')

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)