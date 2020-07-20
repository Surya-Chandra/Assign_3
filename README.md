# Assign_3

Hello,

To access the Role based control app run the main.py using python interpreter. You get the following output:

Hello! Please select an option:

Enter 1 to Add user: Select this option to add a new user which is unique in database. 

Enter 2 to Delete user: Select this optio to delete a user from the database.

Enter 3 to Update user details: Select this option to update a user record from the database.

Enter 4 to access data: Select this option to access the resources in database. You need to enter your username and the required operation you want to perform i.e. read , write or delete. You should have the appropriate access level to perform the operation.

Enter 5 to assign role: Select this option to assign the roles for a user. You need to enter the username for the user here. A single user can have multiple roles and based on these roles the access levels are assigned to the user.

Enter 6 to remove role: Select this option to remove the roles from a given user. You need to enter the username for the user here. You can remove multiple roles of a user from the database. This also modifies the access levels based on role removal.

Enter 7 to exit

Following points are to be Noted:

The role based access control was developed on a local server.

Add user, delete user , update user and access resource from the database were imported from pre-created functions.

#Following is the problem statement:

Role Based Access Control:

Implement a role-based authentication system. System should be able to assign a role to user and remove a user from the role. Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE) Resource Storage: Database (PostgreSQL or Mongo) Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource system should be able to tell whether user has access or not.
