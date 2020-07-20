from mongoengine import Document, StringField, ListField
from localconnect.localconnect import makeconnection

makeconnection()


class User(Document):
    """username : username unique to the database"""
    username = StringField(unique=True, required=True, max_length=10)
    meta = {'allow_inheritance': True}


class accesslevel(User):
    """ roles : list of roles assigned to the user
        actions : list of all the access levels available to the user
    """
    roles = ListField(StringField())
    actions = ListField(StringField())


if __name__ == "__main__":

    while True:
        print("Hello! Please select an option")
        print("Enter 1 to Add user:")
        print("Enter 2 to Delete user:")
        print("Enter 3 to Update user details:")
        print("Enter 4 to access data:")
        print("Enter 5 to assign role")
        print("Enter 6 to remove role")
        print("Enter 7 to exit")
        option = input("Please enter your choice:")
        if option == "1":
            from UserOperations.UserOperationFunctions import deleteuser
            user = adduser()
            user.save()
        elif option == "2":
            from UserOperations.UserOperationFunctions import adduser
            deleteuser()
        elif option == "3":
            from UserOperations.UserOperationFunctions import updateuser
            updateuser()
        elif option == "4":
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                enter = input("Enter r to Read, w to write and d to delete:")
                if enter in obj.actions:
                    from UserOperations.UserOperationFunctions import accessdata
                    accessdata(enter)
                else:
                    print("You don't have the required access level")
            else:
                print("user not found")

        elif option == "5":
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                from UserRoleFunctions.UserRoleFunctions import addrole
                addrole(obj)
            else:
                print("user not found")
        elif option == "6":
            name = input("Please enter the username:")
            obj = User.objects(username=name).get()
            if obj:
                from UserRoleFunctions.UserRoleFunctions import removerole
                removerole(obj)
            else:
                print("user not found")
        elif option == "7":
            exit()
        else:
            print("Please enter a valid choice")

        option = input('Choose 1 to quit and 2 to continue:')
        if option == "1":
            exit()
        else:
            continue
