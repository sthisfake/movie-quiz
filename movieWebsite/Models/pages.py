from cgitb import html
from django.shortcuts import render
from requests import request


def quizPage(request) :
    return render( request, "quiz.html" , {} )