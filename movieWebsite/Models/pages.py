from cgitb import html
import imp
from urllib.parse import uses_relative
from django.shortcuts import render , redirect
from requests import request
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .classes import User


def homePage(request) :
    return render(request , "home.html" , {} )    

def signUp(request):

    if request.method == 'POST':

        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName' )
        UserName = request.POST.get('UserName')
        email = request.POST.get('email' )
        password = request.POST.get('password')
        user = User(firstName , lastName , UserName  , email , password )

        checkUserName = user.checkIfExistUsername()
        if checkUserName == True :
            context = {'userError' : 'this user name already taken , try again'}
            return render(request , 'signUp.html'  , context )


        checkEmailExist = user.checkIfEmailExistDataBase()    
        if checkEmailExist == True:
            context = {'emailError' : 'this email has already have an account , try again'}
            return render(request , 'signUp.html'  , context ) 

        
        checkEmailValidation = user.checkEmailValidation()   
        if checkEmailValidation == False :
            context = {'emailError' : 'please write a correct email'}
            return render(request , 'signUp.html'  , context )      


        checkEmailExistForReal = user.checkEmailReallExistence()   
        if checkEmailExistForReal == False:
            context = {'emailError' : 'this email doesnt exist '}
            return render(request , 'signUp.html'  , context )  

        isValid , massage = user.checkIfPasswordIsVallid()  
        if isValid == False:
            context = {'passError' : massage}
            return render(request , 'signUp.html'  , context )  

        user.addToUsers()
        redirect('user')
    return render(request , "signUp.html" ,{} )    

def login(request):
    if request.method == 'POST':
        userNameOrPass = request.POST.get('userNameOrPass')
        password = request.POST.get('password')
    return render(request , "login.html" , {})  

def userPage(request):
    return render(request , 'user.html' , {})




def quizPage(request) :
    # return render( request, "quiz.html" , {} )
    return render(request , "quiz.html" , {})






