# Assignment: Checkerboard
# ==========================

# Objectives:
# ------------
# Continue to learn how to pass information from the url to the route
# Get comfortable passing information from the route to the template
# Understand how to use for loop properly in the template
# Recognize the value of creating a html/css first and then adding logic/code


# Write a program that generates an HTML page that looks like a checkerboard.  
# For this assignment, you're allowed to use <table> if you want.  
# You could use <div> if desired.  
# (Note: During Web Fundamentals, we discouraged you from using <table> as we 
# didn't want you to use <table> to position different contents of your website on 
# different parts of the table.  For this assignment however, you are allowed to use <table>.)

# Your program should have the following output

# http://localhost:5000 - should display 8 by 8 checkerboard

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, please remember to convert it to integer 
# first (so that you can use x or y in a for loop)

# Video Demo - please watch this after you've worked on the assignment for 45 minutes
# If you watch this video without first struggling on your own to do this 
# assignment, this video won't add so much value for you.  
# Please first spend 45 minutes to complete the assignment on your own. 
# After you've spent 45 minutes on your own, then please watch this video.  
# Again please watch after you've first spent 45 minutes on your own doing the assignment.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if (path==""):
        print("-- index: blank path: display 8x8 --")
        return render_template("checker_index.html", bd_width=8, bd_height=8, colorplayblack='black', colorplayred='red')
    else:
        print("-- index: unexpected path: {" + path + "} --> display instructions --")
        return render_template("checker_instructions.html")

@app.route('/<int:intx>/<int:inty>/')
def display_checkerboard(intx,inty):
    print("-- display_checkerboard intx=" + str(intx) + ", inty=" + str(inty) + " --")
    return render_template("checker_index.html", bd_width=intx, bd_height=inty, colorplayblack='black', colorplayred='red')

@app.route('/<int:intx>/<int:inty>/<color1>/<color2>/')
def display_checkerboard_colors(intx,inty,color1,color2):
    print("-- display_checkerboard colors intx=" + str(intx) + ", inty=" + str(inty) + ", color1=" + color1 + ", color2=" + color2 + " --")
    return render_template("checker_index.html", bd_width=intx, bd_height=inty, colorplayblack=color1, colorplayred=color2)

# @app.route('/')
# def index():

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mo





# OUTPUT: 
# -- display_checkerboard colors intx=10, inty=10, color1=cyan, color2=lime --
# 127.0.0.1 - - [07/Jun/2018 13:59:37] "GET /10/10/cyan/lime/ HTTP/1.1" 200 -
# -- index: blank path: display 8x8 --
# 127.0.0.1 - - [07/Jun/2018 13:59:43] "GET / HTTP/1.1" 200 -
# -- display_checkerboard colors intx=10, inty=10, color1=cyan, color2=lime --
# 127.0.0.1 - - [07/Jun/2018 13:59:47] "GET /10/10/cyan/lime/ HTTP/1.1" 200 -
# -- index: unexpected path: {1adsa} --> display instructions --
# 127.0.0.1 - - [07/Jun/2018 14:01:00] "GET /1adsa HTTP/1.1" 200 -

