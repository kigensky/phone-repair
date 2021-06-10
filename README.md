# Phone-Repair
## Author  
  
* Victor Kigen
  
# Description  
This is a flashcard django application intended to be used as an aid in memorization.
  
##  Live Link  
 Click [View Site](https://fundi-online.herokuapp.com/)  to visit the site
 


## User Story

* user has to sign into the application to start using.
* User can post a problem they have with their phone
* User can Search for a solution with the cases available
* User can view repairs and solutions.
* User can upvote or downvote on the solution they are given"
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/kigensky/phone-repair
```
##### Navigate into the folder and install requirements  
 ```bash 
cd PHONE-REPAIR pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations phone-repair
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vickigen@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/kigensky/pic-galery/blob/main/LICENCE)  
* Copyright (c) 2021 **Victor Kigen**