from flask import Flask
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnerr import connectToMySQL

app = Flask(__name__)

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('mydb')

# now, we may invoke the query_db method
query = "SELECT * FROM users;"
sqldata = mysql.query_db(query)
# print("all the users", sqldata)

print("mysql>>> mydb::users::"+query)
for i in sqldata: 
    print(i)
    # for k in i:
    #     print(i,k,i[k])  


if __name__ == "__main__":
    app.run(debug=True)