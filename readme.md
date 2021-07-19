## Author
* Anne Chege
### award-app
award-app is a platform where users  can view initial project 

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Install python
  - Install and activate virtual
  - Setup Database
  - Install Django


### Installation Process
Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.8```.
  - ```python --version``` to confirm that python has been installed.
##### Git clone the project on your current directory by:
  - ```git clone https://github.com/annechege/awards-app.git```.
##### Install virtual environment using python:
  - ```python3.8 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.8``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z or exit()``` to get out of the shell,
##### After ensuring you have all the above
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.

### User Stories
As a user, I would like to sign in to the application to start using it.
As a user, I would like to upload my pictures to the application.
As a user, I would like to see my profile with all my pictures.
As a user, I would like to like a picture and leave a comment on it.



### Behavior Driven Development

##### Given that a user sign-up with the correct details, and use those details to login successfully, then they should be able to access the application and it's features.
##### Given that the user has uploaded a photo, then, the application should display the photo uploaded.
##### Given that a user has logged in, created a profile and posted a picture, then they  should be able to view their profile and all the photos they've posted.
##### Given that a user has an account, then they should be able to follow other users, see the photos of the users they are following on their timeline and also like and comment on those photos.



### Technologies Used
Python
Django
PostgreSQL
HTML


### Licence
[MIT](LICENSE) 