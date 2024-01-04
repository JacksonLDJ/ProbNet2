
# ProbNet 2

This Django application has been created for a University Assignment. It uses Python's NMAP library to perform NMAP scans and also has the function of performing a network sweep. Once scanned, this information is saved to a SQL Workbench Database. This can also be views within the application.




## Programming Frameworks and Languages

* Django
* Python
## Database

* MySQL Workbench
## Installation

This application uses NMAP, which must be installed on your local system, this can be installed [here.](https://nmap.org/download.html)

You then need to create a virtual envrionment for Django, which can be done be following the official documentation [here.](https://docs.djangoproject.com/en/3.1/intro/contributing/#getting-a-copy-of-django-s-development-version) You then need to activate the envrionment.

Install all of the application dependencies with the command - pip install -r requirements.txt

To create the database for this application, you will need to install MySQL Workbench from [here.](https://dev.mysql.com/downloads/workbench/) You will then need to create your database with the following information:

* 'HOST': 'localhost', 'PORT': '3306', User: Root, Password: aJ941S@>A/<+
* This application uses envrion, so make sure you enter PASSWORD=aJ941S@>A/<+ in your envrion file and then in settings.py file, enter 'PASSWORD': env("PASSWORD"), under the DATABASES section.

Finally, to create the database and tables, in your terminal, browse to the ProbNet2 and type python manage.py makemigration and then python manage.py migrate.



## How to run it

In your terinal, type: cd .\ProbNet2\ and then python manage.py runserver.

A web page will load, and the login page appears. Enter your login details and then use the app.

In Perform a device scan, you can simply enter an IP address, this will then run an NMAP scan and write the information back to your SQLWorkbench. 

in Netsweeper scan, you can 