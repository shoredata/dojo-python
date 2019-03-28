from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def show(request):
    response = "Hello, I am your second request!"
    return HttpResponse(response)    

def month_archive(request, username):
    # entering: http://localhost:8000/bio/bobsmith/
    # prints:   month_archive: bobsmith
    response = "Hello, I am your third request!"
    print("month_archive: " + username)
    return HttpResponse(response)        

def get_date(request, year, month):
    # entering: http://localhost:8000/login/2018/12/
    # prints:   month_archive: Hello Dave 2018 12
    response = "Hello Dave " + str(year) + " " + str(month)
    print("month_archive: " + response)
    return HttpResponse(response)        