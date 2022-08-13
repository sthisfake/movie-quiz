from cgitb import html
import imp
from multiprocessing import context
from os import stat
import re
from urllib.parse import uses_relative
from django.shortcuts import render , redirect
from requests import request
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .classes import User , checkLogin , checkUserAuthenticationWithEmail , checkUserAuthenticationWithUserName
from copy import deepcopy




def homePage(request) :
    return render(request , "home.html" , {} )    

def signUp(request):

    if request.method == 'POST':
        status = False
        context={}

        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName' )
        UserName = request.POST.get('UserName')
        email = request.POST.get('email' )
        password = request.POST.get('password')
        user = User(firstName , lastName , UserName  , email , password )

        checkUserName = user.checkIfExistUsername()
        if checkUserName == True :
            context['userError'] = 'this user name already taken , try again'
            status = True

        checkEmailExist = user.checkIfEmailExistDataBase()    
        if checkEmailExist == True:
            context['emailError']  = 'this email has already have an account , try again'
            status = True

        checkEmailValidation = user.checkEmailValidation()   
        if checkEmailValidation == False :
            context['emailError'] = 'please write a correct email'
            status = True

        checkEmailExistForReal = user.checkEmailReallExistence()   
        if checkEmailExistForReal == False:
            context['emailError'] = 'this email doesnt exist '
            status = True

        isValid , massage = user.checkIfPasswordIsVallid()  
        if isValid == False:
            context['passError'] = massage
            status = True
        
        # TODO use ajax to update sign up error
        if status == True :
            return render(request , "signUp.html" ,context)

        user.addToUsers()
        global currentUser 
        currentUser = deepcopy(user)
        return redirect('/user')    
    return render(request , "signUp.html" ,{} )    



def login(request):
    if request.method == 'POST':

        userNameOrPass = request.POST.get('userNameOrPass')
        password = request.POST.get('password')

        check = checkLogin(userNameOrPass , password )
        if check == False :
            context = {'passEror' : 'user name or password is wrong'}
            return render(request , 'login.html' , context )


        if check == 'email' :
            valid , user = checkUserAuthenticationWithEmail(userNameOrPass , password)
            if valid == False :
                context = {'passEror' : 'password is wrong'}
                return render(request , 'login.html' , context ) 
            else :
                global currentUser
                currentUser = deepcopy(user)
                return redirect('/user')    


        if check == 'userName':
            valid  , user = checkUserAuthenticationWithUserName(userNameOrPass , password)
            if valid == False :
                context = {'passEror' : 'password is wrong'}
                return render(request , 'login.html' , context )     
            else :
                currentUser = deepcopy(user)
                return redirect('/user')     


    return render(request , "login.html" , {})  



def userPage(request):
    name = currentUser.getFistName() + currentUser.getLastName()
    context = {'firstName' : name}
    return render(request , 'user.html' , context)




def quizPage(request) :
    return render(request , "quiz.html" , {})






