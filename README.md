
--- TABLE OF CONTENTS ---

    .DEALER_FEEDBACK
    .FILE STRUCTURE
    .FILES
    .RUNNING 
    .CONTACT

DEALER_FEEDBACK:

This is a Flask app that uses PostgreSQL as a database. It allows hypothetical users to rate and comment on the dealer they interacted with and stores those comments in the database. At the same time it sends confirmation emails to the users containg the ratings and comments they made.

You can use it here: https://dry-retreat-32543.herokuapp.com/

This app is based on this tutorial https://www.youtube.com/watch?v=w25ea_I89iM


FILE STRUCTURE:

       {Root}
        |
        +----{static}
        |     |
        |     +----logo.png
        |     |
        |     +----style.css
        |
        +----{templates}
        |     |
        |     +----index.html
        |     |
        |     +----success.html
        |     |
        |     +----list_comments.html
        |
        +----.gitignore               
        |
        +----app.py                   
        | 
        +----send_mail.py             
        |
        +----Pipfile                  
        |
        +----Pipfile.lock
        |
        +----Procfile                 
        |
        +----requirements.txt         
        |
        +----runtime.txt              
        |
        +----README.md

FILES:

* index.html >         Main page and holds the form.
* success.html >       Redirects here if the form has been submitted correctly. 
* list_comments.html > Displays all the comments.
* app.py >             The app itself. Establishes the database, table, server, form.
* send_mail.py >       Module that contains the send_mail() function.
* .gitignore >         Lists of files Git should ignore.
* Pipfile >            Specify the packages requirements.
* Pipfile.lock >       Specify the version of the required packages.
* Procfile >           Declares how the app must be run (uses gunicorn to deploy in heroku)
* requirements.txt >   Specify the dependencies needed.
* runtime.txt >        Secifies what Python version is needed.

RUNNING:

To run it locally in development mode, you have to change in 'app.py' the variable "ENV = 'prod'" to "ENV = 'dev'"

After setting the database, it is necessary to create the table 'feedback' that will hold all the information the user introduces. To do that, you have to open the Python interpreter and run the following:

>from app import db

>db.create_all()

>exit()


CONTACT:

Author: Jorge Martin Joven;
Email: jmartinjoven@gmail.com; 
Github: https://github.com/JorgeMJ 
