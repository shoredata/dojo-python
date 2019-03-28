# Assignment: Playground
# =======================

# Objectives:
# ------------
# Get comfortable passing information from the route to the template
# Understand how to display information passed from the route in the template file
# Get comfortable with using for loops in the template file
# Get comfortable with using if statements in the template file

# Inline CSS
# For this particular assignment, please don't worry about having to create an external 
# css stylesheet, as we haven't taught you yet how to use/create static files.  
# Instead, please use internal css stylesheet approach like below 

# <head>
# <style>
# body {
#     background-color: light blue;
# }
# h1 {
#     color: maroon;
#     margin-left: 40px;
# } 
# </style>
# <head>
# <body>
#     <h1>Hello World</h1>
# </body>
# Also see: https://www.w3schools.com/css/css_howto.asp

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    print("-- index: display default index.html --")
    return render_template("play_index.html", phrase="hello", times=5, boxes_count=0, colorplay="blue")

# Level 1 Playground
# When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes.  
# Please use a template to render this.
@app.route('/play/')
def play_only():
    print("-- index/play: display 3 boxes --")
    return render_template("play_index.html", phrase="hello", times=1, boxes_count=3, colorplay="blue")



# Level 2 Playground
# When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times.  
# For example, localhost:5000/play/7 should display these blue boxes 7 times.  
# Calling localhost:5000/play/35 would display these blue boxes 35 times.  
# Please remember that x originally is a string, and if you want to use it as an integer, you must 
# first convert it to integer using int().  For example int("7") returns 7.
@app.route('/play/<int:countp>/')
def play_countp(countp):
    print("-- index/play/count: display 'count' boxes --")
    return render_template("play_index.html", phrase="hello", times=1, boxes_count=countp, colorplay="blue")



# Level 3 Playground
# When a user visits localhost:5000/play/(x)/(color), have it display beautiful 
# looking boxes x times, but this time where the boxes appear in (color).  
# For example, localhost:5000/play/5/green would display 5 beautiful green boxes.  
# Calling localhost:5000/play/35/red would display 35 beautiful red boxes.
@app.route('/play/<int:countp>/<colorp>/')
def play_countp_color(countp,colorp):
    print("-- index/play/count/color: display 'count' boxes with boder in 'color' --")
    return render_template("play_index.html", phrase="hello", times=1, boxes_count=countp, colorplay=colorp)



if __name__=="__main__":
    app.run(debug=True)



# OUTPUT:
# (py3Env)
# 08:46:13 bart ~/projects/cd/python/flfun/hello_flask
# $ python playground.py
#  * Serving Flask app "playground" (lazy loading)
#  * Environment: production
#    WARNING: Do not use the development server in a production environment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 151-374-095
# -- index/play: display 3 boxes --
# 127.0.0.1 - - [07/Jun/2018 08:47:01] "GET /play/ HTTP/1.1" 200 -
# -- index: display default index.html --
# 127.0.0.1 - - [07/Jun/2018 08:47:07] "GET / HTTP/1.1" 200 -
# -- index/play/count: display 'count' boxes --
# 127.0.0.1 - - [07/Jun/2018 08:47:30] "GET /play/9 HTTP/1.1" 200 -
# -- index/play/count/color: display 'count' boxes with boder in 'color' --
# 127.0.0.1 - - [07/Jun/2018 08:47:44] "GET /play/6/orange HTTP/1.1" 200 -
