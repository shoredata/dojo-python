import datetime
import re
from flask import Flask, render_template, request, redirect, session, flash, json
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconn import connectToMySQL

app = Flask(__name__)
app.secret_key = "789@#$^&#$n789*&^*&^*&^";

# myquery = "select CONCAT(clients.first_name, ' ', clients.last_name) as client, \
#     count(*) as leadcount \
#     from leads \
#     inner join sites on leads.site_id = sites.site_id \
#     inner join clients on sites.client_id = clients.client_id \
#     where registered_datetime >='2011/01/01 00:00:00' AND registered_datetime <='2011/12/31 23:59:59' \
#     group by clients.client_id \
#     order by clients.client_id asc; "
    
myquery = " \
    select count(*) as leadcount, \
        CONCAT(clients.first_name, ' ', clients.last_name) as client \
    from leads \
        inner join sites on leads.site_id = sites.site_id \
        inner join clients on sites.client_id = clients.client_id \
    group by clients.client_id \
    order by clients.last_name asc;"
    # -- where registered_datetime >='2011/01/01 00:00:00' AND registered_datetime <='2011/12/31 23:59:59'
mychartquery = " \
    select count(*) as value, \
        CONCAT(clients.first_name, ' ', clients.last_name) as client \
    from leads \
        inner join sites on leads.site_id = sites.site_id \
        inner join clients on sites.client_id = clients.client_id \
    group by clients.client_id \
    order by clients.last_name asc;"



# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
dbname='lead_gen_business'
mysql = connectToMySQL(dbname)

def savesession(key,value,type0str1int=0):
    if type0str1int == 0:
        session[key] = str(value)
    else:
        session[key] = int(value)
    return 

def initsession():
    if 'datestart' not in session:
        session['datestart'] = ''
        session['dateend'] = ''
    return

def clearsession():
    session.clear()
    return

@app.route('/')
def index():
    initsession()
    print(myquery)
    allresults = mysql.query_db(myquery)
    print("mysql >> " + dbname + "::")
    chartresults = mysql.query_db(mychartquery)
    chart = { "chart": { "type": "pie", "title": "New Leads by Customer", "data": chartresults, "container": "chart_container" } }
    return render_template('index.html', clients = allresults, chartData = json.dumps(chart))













if __name__ == "__main__":
    app.run(debug=True)