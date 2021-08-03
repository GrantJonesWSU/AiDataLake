# AiDataLake Librarian

This document contains the installation steps for this software and the different packages, libraries, and tools necessary to run the application.

Download the source code for this project either through a zip file or through GitHub. 

Make this folder accessible by unzipping it if zipped. 

------------------------------------------------------

We need to install visual studio code first after downloading the source code for the project. 

Visual studio code can be downloaded from code.visualstudio.com for the appropriate operating system.

Once visual studio is installed, make sure that it has the following extensions installed from the extensions tab on the left hand side:
-Python, author: Microsoft
-Pylance, author: Microsoft
-SQLite, author: alexcvzz

Once this is completed, open the project folder in visual studio code.

------------------------------------------------------

The next step in installation is to make sure that a version of Python is installed on you local machine. We recommend version 3.8 or newer. You can download this from python.org or if you are on a linux or mac you can run the following from the terminal in VS code:
Linux - from the terminal run "sudo apt install python3-pip"
macOS - from Homebrew run "brew install python3"

If you are running Windows, you are going to want to make sure that the location of your Python interpreter is in you PATH environment variable.

------------------------------------------------------

Next we are going to set up the virtual enviornment to be able to run this application. 

We will do this through the terminal in VS code again.

For different operating systems the steps are slightly different to set up the virtual environment, so follow the next step according to your own.

Linux:
>sudo apt-get install python3-venv
>python3 -m venv env

macOS:
>python3 -m venv env

Windows:
>python -m venv env

------------------------------------------------------

Now we are going to set up the python interpreter to the virtual environment.

Select "Command Palette" from the "view" dropdown menu at the top of VS code, then type in "Python: Select Interpreter" and click on this option.

Now select the option that contains ('env': venv) as your interpreter. This may require a refresh.

Now when you open a new terminal from the terminal dropdown menu at the top of VS code, it should open at the bottom with (env) at the beginning of the command line.

------------------------------------------------------

Now we are going to set up the packages required to run this application.

Install the packages from the new virtual environment command line with the following code:
>pip install -r requirements.txt

------------------------------------------------------

Let's set up the database now.

Run the following code from the VS code virtual enviornment terminal:
>python manage.py migrate

This should create the database db.sqlite3 in the project folder.

------------------------------------------------------

The final step in installation is to add the corpus information to the application database.

open the file corpus.sql in the sql_files folder. 

Once open, right click anywhere in that open file and select "Run Query," which should add this information to the database. 

------------------------------------------------------

Now you are ready to use this application. 

To run this, enter the following code from the VS code virtual environment terminal
>python manage.py runserver

Once this completes, ctrl+left-click on the http link in the terminal and this should open the application in you preferred browser.