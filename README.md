# Harvard Project 

### Web Programming with Python and JavaScript


Navbar includes all the options for user - login, registration and log out.
When the user logs in, he gets to a welcome page that displays his username and then a search bar where he can input the city or a zipcode for his info search.

models.py  --> create the databases schema necessary to interact with our 3 databases

application.py --> all the logic and routing of the flask application

import.py --> takes the data from zips.csv and uploads it to a database

helpers.py --> includes a file apology. html that shows error messages

In the templates folder, there are all the htmls included such as the page for registration, login or the main index and hello page. All images and css files are in files.

Run in command line:
```bash
flask run
```
