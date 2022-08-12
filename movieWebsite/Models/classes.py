from validate_email_address import validate_email
import re

allUsers = []

class User():
    
    def __init__(self , firstName , lastName , userName , email , password):
        self.firstName = firstName
        self.lastName  = lastName
        self.userName  = userName
        self.email     = email
        self.password  = password

    def addToUsers(self) :
        allUsers.append(self)

    def getFistName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def getUserName(self):
        return self.userName

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def setFistName(self , firstName):
        self.firstName = firstName
    
    def setLastName(self , lastName):
        self.lastName = lastName

    def setUserName(self , userName):
        self.userName = userName

    def setEmail(self ,email):
        self.email = email

    def setPassword(self , password):
        self.password = password   

    def addToUsers(self) :
        allUsers.append(self)  

    def getAllUsers(self):
        return allUsers           

    def checkIfExistUsername(self):

        #returns true if it exist 

        sign = False
        for user in allUsers:
            if user.getUserName() == self.userName:
                sign = True 
                return sign
        return sign        

    def checkIfEmailExistDataBase(self):
        #returns true if it exist in database
        sign = False 
        for user in allUsers:
            if user.getEmail() == self.email:
                sign = True
                return sign
        return sign         
            
    def checkEmailValidation(self):
        #return True if the email address is valid 
        isvalid=validate_email(self.email)
        return isvalid

    def checkEmailReallExistence(self):
        #return True if the email address exists 
        isExists = validate_email(self.email, verify=True) 
        return isExists   

    def checkIfPasswordIsVallid(self):
        check = True
        status = False
        password = self.password
        massage = ''
        while check:  
            if (len(password)<8):
                massage = 'password too short'
                break
            elif not re.search("[a-z]",password):
                massage = 'password must contain lower case charactors'
                break
            elif not re.search("[0-9]",password):
                massage = 'password must contain a number'
                break
            elif not re.search("[A-Z]",password):
                massage = 'password must contain upper case charactors'
                break
            else:
                 check=False
                 status = True
                 break
        return status , massage

        


