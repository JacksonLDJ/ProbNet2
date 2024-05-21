
# ProbNet 2

ProbNet 2 is a University of Bolton Assignment project that was completed for SWE5208 - Business Software Development module in my Digitial Technologies Systems: Cybersecurity degree apprenticeship. The module was split into two assignments, the first being the planning and preperation of the web application including the design of the database to be used. The second half was to implement this plans and then present the work to the "client". Explaining the features and the design choices made. Ultimately this piece of work uses Django for the framework, taking advantage of their ORM and back-end for their user creation and being able to make changes to the SQL Database within the app itself. My first web application which is basic in it's scope but met the onjectives set by the module guide. 




## Programming Frameworks and Languages

* Django
* Python

## Design

Tailwinds CSS

## Database

* MySQL Workbench
* 
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

A web page will load and the login page appears. Enter your root login details to access the app.

Once signed in, you're then able to create customers for the network discovery part of the web application. There are certain mandatory fields, including the IP Range for the company. This newly created customer is then written back to the SQL Database.

Once a scan has been performed, it is then possible to browse the discovered hosts and perform in-depth scans including scanned ports.

