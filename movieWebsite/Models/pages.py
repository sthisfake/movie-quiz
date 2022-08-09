from cgitb import html
from django.shortcuts import render
from requests import request
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm



def homePage(request) :
    return render(request , "home.html" , {} )    

def signUp(request):
    return render(request , "signUp.html" ,{} )    

def login(request):
    return render(request , "login.html" , {})  

def userPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data.get('firstName')
            print(firstName)
            return render(request , 'user.html' , {"firstName" : "pouya"}) 
    print(form)           
    return  render(request , 'user.html' , {"firstName" : "reza"})  




def quizPage(request) :
    # return render( request, "quiz.html" , {} )
    return render(request , "quiz.html" , {})






