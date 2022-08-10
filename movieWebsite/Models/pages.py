from cgitb import html
import imp
from urllib.parse import uses_relative
from django.shortcuts import render
from requests import request
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .classes import User


def homePage(request) :
    return render(request , "home.html" , {} )    

def signUp(request):
    return render(request , "signUp.html" ,{} )    

def login(request):
    if request.method == 'POST':
        userNameOrPass = request.POST.get('userNameOrPass')
        password = request.POST.get('password')
    return render(request , "login.html" , {})  

def userPage(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName' )
        UserName = request.POST.get('UserName')
        email = request.POST.get('email' )
        password = request.POST.get('password')
        user = User(firstName , lastName , UserName  , email , password )
        user.addToUsers()
    return render(request , 'user.html' , {})




def quizPage(request) :
    # return render( request, "quiz.html" , {} )
    return render(request , "quiz.html" , {})






