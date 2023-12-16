# Test App | Django

This project contains two main parts :
the first one consists of a Rest Api that allows users to manage a collection of books
The second one is a task manager app that presents the following features :
    - It allows multiple user registration
    - each user registered can have mutiple roles including manager and worker roles
    - only the users with manager role can create new tasks

Notes:
    - The current version doesn't create the manager and worker roles automatically 
       so you have to create them manually via the admin panel -> Roles admin view

  To launch the app, you either use docker container when opening the project in code editor,
so you only need to install docker on your machine along with docker compose and thereafter
click on "Reopen in Container" and eventually you run "Launch Test App"
another way is to create a virtual env and to install the dependencies of the project inside it 
and then you run "python manage.py runserver" command
