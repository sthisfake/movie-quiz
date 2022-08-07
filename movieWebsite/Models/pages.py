from cgitb import html
from django.shortcuts import render
from requests import request
from django.http import HttpResponse


def quizPage(request) :
    # return render( request, "quiz.html" , {} )
    return render(request , "quiz.html" , {})


def homePage(request) :
    return render(request , "home.html" , {} )    


