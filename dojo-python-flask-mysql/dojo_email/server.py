import datetime
import re
import bcrypt
import random        

from flask import Flask, render_template, request, redirect, session, flash
from mysqlconn import connectToMySQL

app = Flask(__name__)        
app.secret_key = "a%$%$sf#$%^&*())"

# password = b"super secret password"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# if bcrypt.checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
dbname='dojo_wall'
mysql = connectToMySQL(dbname)


def initsession():
    if 'namefirst' not in session:
        clearsession()
        session['namefirst'] = ''
        session['namelast'] = ''
        session['email'] = ''
        session['userhash'] = ''
        session['userid'] = ''
    return

def clearsession():
    session.clear()
    return

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


def does_user_exist():
    exists = False
    tablename = 'users'
    # in this simple exercise all 3 fields must exist
    myquery = "SELECT * FROM " + tablename + " WHERE "
    myquery += " email = '" + request.form['email'] + "' "
    myquery += " ;"
    print(myquery)
    myresults = mysql.query_db(myquery)
    print("mysql >> " + dbname + "::" + tablename + "::"+myquery)
    for i in myresults: 
        print(i)
        exists = True
    
    if not exists:
        flash("does_user_exist::NOPE :(", "login")

    return exists

def is_user_admin(myemail):
    exists = False
    tablename = 'users'
    # in this simple exercise all 3 fields must exist
    myquery = "SELECT * FROM " + tablename + " WHERE "
    myquery += " email = '" + myemail + "' AND "
    myquery += " user_level = '9' ;"
    print(myquery)
    myresults = mysql.query_db(myquery)
    print("mysql >> " + dbname + "::" + tablename + "::"+myquery)
    for i in myresults: 
        print(i)
        exists = True
    return exists


def is_email_form_field_valid():
    myreturn = True
    if 'email' in request.form:
        if len(request.form['email']) < 1:
            flash("ERROR: Email must not be blank",'email')
            myreturn = False
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("ERROR: Invalid Email Address",'email')
            myreturn = False
    else:
        flash("ERROR: Email must not be blank",'email')
        myreturn = False
    return myreturn

def is_name_form_field_valid(desc, field):
    myreturn = True
    if field in request.form:
        if len(request.form[field]) < 1:
            flash("ERROR: " + desc + " must not be blank",field)
            myreturn = False
        elif not NAME_REGEX.match(request.form[field]):
            flash("ERROR: Invalid " + desc + " - Alpha Characters Only",field)
            myreturn = False
    else:
        flash("ERROR: " + desc + " must not be blank",field)
        myreturn = False
    return myreturn

def is_password_form_field_valid(desc, field):
    myreturn = True
    if field in request.form:
        if len(request.form[field]) < 1:
            flash("ERROR: " + desc + " must not be blank",field)
            myreturn = False
        elif not PASSWORD_REGEX.match(request.form[field]):
            flash("ERROR: Invalid Character in " + desc, field)
            myreturn = False
    else:
        flash("ERROR: " + desc + " must not be blank", field)
        myreturn = False
    return myreturn

def does_form_password_match_database():
    exists = False
    tablename = 'users'

    mypassword = request.form['password'].encode('utf-8')

    myquery = "SELECT * FROM " + tablename + " WHERE "
    myquery += " email = '" + request.form['email'] + "' "
    myquery += " ;"
    print(myquery)
    myresults = mysql.query_db(myquery)
    print("mysql >> " + dbname + "::" + tablename + "::"+myquery)
    for i in myresults: 
        print("????", i['passwordhash'])
        if bcrypt.checkpw(mypassword, i['passwordhash'].encode('utf-8')):
            print("It Matches!!!!!!!!!!!!!!!!!!!!!!!!")
            exists = True
        else:
            print("It Does not Match :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")

    if not exists:
        flash("does_form_password_match_database::NOPE :(", "password")

    return exists



def update_session_with_user_data():
    myquery = "SELECT * FROM users WHERE email = '" + session['email'] + "' ;"
    # print(myquery)
    myresults = mysql.query_db(myquery)
    # print("mysql >> " + dbname + "::" + tablename + "::"+myquery)
    print("======================================================")
    # print(myresults)
    # [{'id': 1, 'namefirst': 'BARTON', 'namelast': 'SCHAEFER', 'email': 'shoredata@gmail.com', 'passwordhash': '$2b$12$/Rw4k/ER/2rnTgtb.7M/4O08lFEKMaOR8lAu66he82w6qqnslRMRa', 'user_level': '9', 'warning_level': '0', 'expires_at': None, 'created_at': datetime.datetime(2018, 6, 12, 17, 31, 46), 'updated_at': datetime.datetime(2018, 6, 12, 17, 31, 46)}]
    session['email'] = myresults[0]['email']
    session['namefirst'] = myresults[0]['namefirst']
    session['namelast'] = myresults[0]['namelast']
    session['userid'] = myresults[0]['id']
    print(session)
    return


def get_msg_query(myfield, myid):
    this_query = "SELECT  messages.message, \
        messages.created_at as sent_on, \
        receiver.email as to_email,  \
        sender.email as from_email, \
        CONCAT(receiver.namefirst, ' ', receiver.namelast) as to_name, \
        CONCAT(sender.namefirst, ' ', sender.namelast) as from_name, \
        messages.to_id as to_id,  \
        messages.from_id as from_id  \
        FROM messages \
        LEFT OUTER JOIN \
        users sender ON messages.from_id = sender.id \
        LEFT OUTER JOIN \
        users receiver ON messages.to_id = receiver.id \
        WHERE \
        messages." + myfield + " = " + myid + ";"
    return this_query




# ##########   DEFAULT ROUTE   ########################################################################
# ########################################################################################
# our index route will handle rendering our form
# @app.route('/')
# def index():
#     return render_template("index.html")
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if (path==""):
        print("-- index: blank path: default --")
    else:
        print("-- index: unexpected path: {" + path + "} --> display 404 --")
    initsession()
    print("Session .. ")
    for x in session:
        print(x+":",session[x])

    tablename = 'users'
    allquery = "SELECT * FROM " + tablename + ";"
    allresults = mysql.query_db(allquery)
    # print(allquery)
    # print("mysql >> " + dbname + "::" + tablename + "::"+allquery)
    # for i in allresults: 
    #     print(i)
    #     for k in i:
    #         print('\t',k,i[k])  
    return render_template('index.html', userslist = allresults)

    # return render_template('index.html')


# ##########   LOGIN ROUTE   ########################################################################
# ########################################################################################
@app.route('/login', methods=['POST'])
def login():
    print("Got Login Post Info")

    session.pop('_flashes', None)

    for x in request.form:
        print(x+":",request.form[x])

    session['email'] = request.form['email']
    bsuccess = True

    ### EMAIL ##########################################
    bsuccess = is_email_form_field_valid()

    ### PASSWORD #######################################
    if bsuccess:
        bsuccess = is_password_form_field_valid("Password", "password")
        if bsuccess:
            print("AAA")
            btestpw =  test_password(request.form['password'])
            if not btestpw[0]:
                flash("ERROR: " + btestpw[1],'password')
                bsuccess = False
            else: 
                print("BBB")
                bsuccess = does_user_exist()
                if bsuccess:
                    print("CCC")
                    bsuccess = does_form_password_match_database()
                    if bsuccess:
                        ### EMAIL VALID, PASSWORD MATCHES, LOGIN OK ##############

                        update_session_with_user_data()

                        # hash(userid + created_at + app.key) ==> hash_in_session
                        print("Session .. ")
                        for x in session:
                            print(x+":",session[x])

                        flash("LOGIN SUCCESSFULL ++", "login")

    if bsuccess:
        if is_user_admin(session['email']):
            print("User IS admin")
            return redirect("/show_admin")
        else:
            print("User is NOT admin")
            return redirect("/show_user")
    else:
        # NOPE, BUT YOU CAN TRY AGAIN
        return redirect('/')


# ##########   SHOW LOGGED IN USER ROUTE   ###############################################
# ########################################################################################
@app.route('/show_user')         
def login_user():
    myemail = session['email']
    myid = str(session['userid'])
    print("USER:{" + myid + ", " + myemail + "}")

    # tablename = 'users'
    # myquery = "SELECT * FROM " + tablename + ";"
    # allusers = mysql.query_db(myquery)
    # print(myquery)
    # # print("mysql >> " + dbname + "::" + tablename + "::"+allquery)

    tablename = 'users'
    myquery = "SELECT * FROM " + tablename + " WHERE email not like '" + myemail + "';"
    otherusers = mysql.query_db(myquery)
    # print(myquery)

    myquery = get_msg_query("to_id", myid)
    mymessages = mysql.query_db(myquery)

    myquery = get_msg_query("from_id", myid)
    mysentmessages  = mysql.query_db(myquery)

    return render_template("welcome.html", adminuserslist = "", otheruserslist = otherusers, rxmessages=mymessages, txmessages=mysentmessages)


# ##########   SHOW LOGGED IN ADMIN ROUTE   ##############################################
# ########################################################################################
@app.route('/show_admin')         
def login_admin():

    myemail = session['email']
    myid = str(session['userid'])
    print("ADMIN:{" +myid + ", " + myemail + "}")

    tablename = 'users'
    myquery = "SELECT * FROM " + tablename + ";"
    allusers = mysql.query_db(myquery)
    print(myquery)
    # print("mysql >> " + dbname + "::" + tablename + "::"+allquery)

    tablename = 'users'
    myquery = "SELECT * FROM " + tablename + " WHERE email not like '" + myemail + "';"
    otherusers = mysql.query_db(myquery)
    # print(myquery)

    myquery = get_msg_query("to_id", myid)
    mymessages = mysql.query_db(myquery)

    myquery = get_msg_query("from_id", myid)
    mysentmessages  = mysql.query_db(myquery)

    return render_template("welcome.html", adminuserslist = allusers, otheruserslist = otherusers, rxmessages=mymessages, txmessages=mysentmessages)




# ##########   REGISTER ROUTE   ########################################################################
# ########################################################################################
@app.route('/register', methods=['POST'])
def register():
    print("Got Register Post Info")

    session.pop('_flashes', None)

    session['namefirst'] = request.form['namefirst']
    session['namelast'] = request.form['namelast']
    session['email'] = request.form['email']
    session['userhash'] = ""
    session['userid'] = ""

    print("Saving .. ")
    for x in session:
        print(x+":",session[x])

    for x in request.form:
        print(x+":",request.form[x])

    if 'ResetUser' in request.form:
        if request.form['ResetUser']=='Reset':
            print("User Request Reset Register Data")
            session.clear()
            return redirect('/')

    ####### VALIDATION ################################

    ### EMAIL ##########################################
    bemail = is_email_form_field_valid()

    ### FIRST NAME#######################################
    bfirstname = is_name_form_field_valid("First Name", "namefirst")

    ### LAST NAME #############################################
    blastname = is_name_form_field_valid("Last Name", "namelast")

    ### PASSWORDS MATCH EACH OTHER ############################
    bpasswordmatch = request.form['password'] == request.form['passwordconfirm']
    if not bpasswordmatch:
        flash("ERROR: Passwords do not match",'password')
        flash("ERROR: Passwords do not match",'passwordconfirm')

    ### PASSWORD VALIDATION ############################
    bpassword = is_password_form_field_valid("Password", "password")
    if bpassword:
        btestpw =  test_password(request.form['password'])
        if not btestpw[0]:
            flash("ERROR: " + btestpw[1],'password')
            flash("ERROR: " + btestpw[1],'passwordconfirm')
            bpassword = False

    if bemail and bfirstname and blastname and bpasswordmatch and bpassword:
        ### INPUT FIELDS ARE VALID, CONTINUE###############################
        # password = b"super secret password"
        # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # if bcrypt.checkpw(password, hashed):
        #     print("It Matches!")
        # else:
        #     print("It Does not Match :(")
        #
        # 1/2. make pass hash to store [ hash = hash (pass, salt) ]
        # 3. if first user set user_level = 9, else user_level = 0
        # 4. warn_level = 0, expires = null
        # 5. created, updated = now
        # 6. fields from form (namefirst, namelast, email)
        #
        # create user in db
        # if success:
        #   clear session, restore e-mail
        # clearsession()
        session['email'] = request.form['email']
        print("Session .. ")
        for x in session:
            print(x+":",session[x])

        # password = b"super secret password"
        # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # if bcrypt.checkpw(password, hashed):
        #     print("It Matches!")
        # else:
        #     print("It Does not Match :(")

        mypassword = request.form['password'].encode('utf-8')
        mypasswordhash = bcrypt.hashpw(mypassword, bcrypt.gensalt())
        if bcrypt.checkpw(mypassword, mypasswordhash):
            print("It Matches!!!")
        else:
            print("It Does not Match :( :(")

        myquery = "INSERT INTO USERS (namefirst, namelast, email, passwordhash, user_level, warning_level, created_at, updated_at) \
            VALUES ( %(namefirst)s, %(namelast)s, %(email)s, %(passwordhash)s, %(user_level)s, %(warning_level)s, now(), now() );"
        print(myquery)
        mydata = {
                'namefirst': request.form['namefirst'],
                'namelast':  request.form['namelast'],
                'email': request.form['email'],
                'passwordhash' : mypasswordhash,
                'user_level' : "9", 
                'warning_level' : "0", 
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now())
        }

        if (request.form['email']!='shoredata@gmail.com'):
            mydata['user_level'] = '0'

        # 'passwordhash' : mypasswordhash.decode('utf-8'),
        print(mydata)
        insert_id = mysql.query_db(myquery, mydata)
        if type(insert_id) is int:
            print("Inserted ID: " + str(insert_id))
            # clearsession()

            flash("ACCOUNT CREATION SUCCESSFULL, PLEASE LOGIN ++", "register")
        else:
            flash("SOMETHING WENT WRONG, OH NO --", "register")


    # always require login
    # WHETHER REG IS OK OR NOT YOU MUST LOGIN
    return redirect('/')


# ##########   NEW MESSAGE ROUTE   #######################################################
# ########################################################################################
@app.route('/new_message', methods=['POST'])
def new_message():
    print("Got new_Message Post Info")

    print("Session::")
    for x in session:
        print(x+":",session[x])

    print("Request::")
    for x in request.form:
        print(x+":",request.form[x])

    if 'ResetMessage' in request.form:
        if request.form['ResetMessage']=='Reset':
            print("User Request Reset New Message Data")
            # session.clear()
            # return redirect('/')
    else:
        if 'Logout' in request.form:
            if request.form['Logout']=='Logout':
                print("User Request Logout")
                session.clear()
                return redirect('/')
        else:
            print("User Submits New Message")
            # INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "a adsf sdf dsa fasdfads", now());
            myquery = "INSERT INTO messages (from_id, to_id, message, created_at, updated_at) \
                VALUES ( %(from_id)d, %(to_id)d, %(message)s, now(), now() );"
            print(myquery)
            mydata = {
                    'from_id': session['userid'],
                    'to_id':  request.form['touserid'],
                    'message': request.form['message'],
                    'created_at': str(datetime.datetime.now()),
                    'updated_at': str(datetime.datetime.now())
            }
            print(mydata)
            insert_msg_id = mysql.query_db(myquery, mydata)
            if type(insert_msg_id) is int:
                print("Message Inserted ID: " + str(insert_msg_id))
                # clearsession()

                flash("MSG CREATION SUCCESSFULL, PLEASE REFRESH", "message")
            else:
                flash("SOMETHING WENT WRONG, OH NO --", "message")









    if is_user_admin(session['email']):
        print("User IS admin")
        return redirect("/show_admin")
    else:
        print("User is NOT admin")
        return redirect("/show_user")





if __name__=="__main__":
    # run our server
    app.run(debug=True) 



# mysql> describe users;
# +---------------+--------------+------+-----+---------+----------------+
# | Field         | Type         | Null | Key | Default | Extra          |
# +---------------+--------------+------+-----+---------+----------------+
# | id            | int(11)      | NO   | PRI | NULL    | auto_increment |
# | namefirst     | varchar(45)  | YES  |     | NULL    |                |
# | namelast      | varchar(45)  | YES  |     | NULL    |                |
# | email         | varchar(45)  | YES  |     | NULL    |                |
# | passwordhash  | varchar(128) | YES  |     | NULL    |                |
# | user_level    | varchar(45)  | YES  |     | NULL    |                |
# | warning_level | varchar(45)  | YES  |     | NULL    |                |
# | expires_at    | varchar(45)  | YES  |     | NULL    |                |
# | created_at    | datetime     | YES  |     | NULL    |                |
# | updated_at    | datetime     | YES  |     | NULL    |                |
# +---------------+--------------+------+-----+---------+----------------+
# 10 rows in set (0.00 sec)

