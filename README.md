# Django - Blog Application

###### A Blog application developed using Django framework

## Features
* User Authentication - Users can register, login and logout
* View ,Create, Edit and Delete Posts
* Blog content is managed with a rich text editor.
* Forms have proper validations built in both at the front end and at the back end.

## Steps to be followed for first time use, Run the following commands

 * git clone https://github.com/gauri890/django-blog-assesment.git
 
 * python -m venv virtual_env
 
 * virtual_env\scripts\activate
 
 * pip install -r requirements.txt
 * python manage.py makemigrations
 * python manage.py migrate
 * python manage.py createsuperuser
   * Enter your desired username, email and password. Make sure you remember them as you'll need them in future.
   eg.

   * Example --> Username: gauri
   Email: gauri@admin.com
   Password: 1234

   All Set! 🤩

* Now you can run the server to see your application up & running 🚀

  * python manage.py runserver

* To exit the environment ❎
  * deactivate
* Every time you want to open the application in browser, make sure you run:
  * source virtual_envarticle-content\Scripts\activate
  * python manage.py runserver

 

