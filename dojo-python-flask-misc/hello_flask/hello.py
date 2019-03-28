# Assignment: Understanding Routing
# ================================

# Objectives:
# ------------
# Practice building a server with Flask from scratch
# Get comfortable with routes and passing information to the routes
# Create a server file that generates 5 different http responses for the following 5 url requests:


from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is


# localhost:5000 - have it say "Hello World!" 
# - Hint: If you have only one route that your server is listening for, it must be your root route ("/")
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    print("hello world")
    return 'Hello World!'  # Return the string 'Hello World!' as a response.copy

# localhost:5000/dojo 
# - have it say "Dojo!"
@app.route('/dojo/')
def do_dojo():
    print("dojo")
    return "Dojo!"

def say(name):
    return 'Hi %s!' % (name)



@app.route('/say/james/') # for a route '/say/____' anything after '/hello/' gets passed as a variable 'name'
def say_hi_j():
    print(say("--james--"))
    return say("--james--")



# localhost:5000/say/flask 
# - have it say "Hi Flask".  Have function say() handle this routing request.
# localhost:5000/say/michael 
# - have it say "Hi Michael" (have the same function say() handle this routing request)
# localhost:5000/say/john 
# - have it say "Hi John!" (have the same function say() handle this routing request)
# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/say/<name>/') # for a route '/say/____' anything after '/hello/' gets passed as a variable 'name'
def say_hi(name):
    print(say(name))
    return say(name)









# localhost:5000/repeat/35/hello 
# - have it say "hello" 35 times! 
# - You will need to convert a string "35" to an integer 35.  To do this use int().  
# For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, it should say "hello" 80 times.
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)
@app.route('/repeat/<int:repeatcount>/<torepeat>/')
def do_repeatb(repeatcount, torepeat):
    print("repeat " + str(torepeat) + ", " + str(repeatcount) + " times")
    # return (torepeat*int(count))
    return str(repeatcount * str(torepeat+'\n'))


@app.route('/success/')
def success():
    print("success")
    return "success"

@app.route('/hello/<name>/') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello "+name

@app.route('/users/<username>/<id>/') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mo







# OUTPUT: 
# (py3Env)
# 20:32:45 bart ~/projects/cd/python/flfun/hello_flask
# $ python hello.py
# __main__
#  * Serving Flask app "hello" (lazy loading)
#  * Environment: production
#    WARNING: Do not use the development server in a production environment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#  * Restarting with stat
# __main__
#  * Debugger is active!
#  * Debugger PIN: 151-374-095
# hello world
# 127.0.0.1 - - [06/Jun/2018 20:32:58] "GET / HTTP/1.1" 200 -
# dojo
# 127.0.0.1 - - [06/Jun/2018 20:33:13] "GET /dojo HTTP/1.1" 200 -
# Hi flask!
# 127.0.0.1 - - [06/Jun/2018 20:33:34] "GET /say/flask HTTP/1.1" 200 -
# Hi michael!
# 127.0.0.1 - - [06/Jun/2018 20:33:39] "GET /say/michael HTTP/1.1" 200 -
# Hi john!
# 127.0.0.1 - - [06/Jun/2018 20:33:44] "GET /say/john HTTP/1.1" 200 -
# repeat hello, 35 times
# 127.0.0.1 - - [06/Jun/2018 20:33:59] "GET /repeat/35/hello HTTP/1.1" 200 -
# repeat dogs, 99 times
# 127.0.0.1 - - [06/Jun/2018 20:35:31] "GET /repeat/99/dogs HTTP/1.1" 200 -
# success
# 127.0.0.1 - - [06/Jun/2018 20:35:52] "GET /success HTTP/1.1" 200 -
# freddy_barnes
# 127.0.0.1 - - [06/Jun/2018 20:36:07] "GET /hello/freddy_barnes HTTP/1.1" 200 -
# john
# 101764
# 127.0.0.1 - - [06/Jun/2018 20:36:17] "GET /users/john/101764 HTTP/1.1" 200 -










