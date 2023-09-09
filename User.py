#Salwa Fayyad 1200430
#Sondos Ashraf 1200905

userList=[[]]
class user:
    def __init__(self, User_id, User_name, User_DoB, Role, Active):
        self.User_id = User_id
        self.User_name = User_name
        self.User_DoB = User_DoB
        self.Role = Role
        self.Active = Active

    def addusers(self, User_id, User_name, User_DoB, Role, Active):
        userList.append([User_id,User_name,User_DoB, Role, Active])

    def printlist(self):
        print(userList)
    
    def getlist(self):
        return userList
    
    def update_user(self, User_id, User_name, User_DoB, Role, Active):
        for user_entry in userList:
            if User_id == user_entry[0]:  # Compare User_id with the User_id in the current user_entry
                user_entry[1] = User_name  
                user_entry[2] = User_DoB  
                user_entry[3] = Role 
                user_entry[4] = Active   
            break 



class Shopper(user):
    def __init__(self, User_id, User_name, User_DoB, Role, Active, Basket, order):
        super().__init__(User_id, User_name, User_DoB, Role, Active)
        self.Basket = Basket
        self.order = order

    def addusers(self, User_id, User_name, User_DoB, Role, Active,Basket,order):
        userList.append([User_id,User_name,User_DoB, Role, Active,Basket,order])

    def printlist(self):
        print(userList)
    
    def getlist(self):
        return userList
    
    def update_user(self, User_id, User_name, User_DoB, Role, Active, Basket, order):
        for user_entry in userList:
            if User_id == user_entry[0]:  # Compare User_id with the User_id in the current user_entry
                user_entry[1] = User_name  
                user_entry[2] = User_DoB  
                user_entry[3] = Role 
                user_entry[4] = Active  
                user_entry[5] = Basket  
                user_entry[6] = order  
            break
        
         
    def __str__(self):
            return f"User ID: {self.User_id}\nUser Name: {self.User_name}\nDate of Birth: {self.User_DoB}\nRole: {self.Role}\nActive: {self.Active}"    
