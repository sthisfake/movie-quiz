


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



