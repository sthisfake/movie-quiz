from typing_extensions import Self


class User(Self):
    
    def __init__(self , firstName , lastName , userName , email , password):
        self.firstName = firstName
        self.lastName  = lastName
        self.userName  = userName
        self.email     = email
        self.password  = password
