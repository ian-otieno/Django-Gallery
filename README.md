# Django-Gallery
This Python/Django gallery website was created on the 27/03/2022

## Description
 This is a django gallery application where users can upload their photos and store according to different locations taken and different category
 
 ## Author
## By **[IAN OTIENO](https://github.com/ian-otieno)**

## User Stories
These are the behaviours/features that the application implements for use by a user and writer.

* User loads the application using the url provided
* The user sees various photos posted
* The user clicks on the photo; photos details page is loaded
* user searches for images by category
* different photos are loaded according to that category
* User filters photos by location and different photos are loaded according to that location
* user clicks on the copy button to copy the link to download images


## Behaviour Driven Development
## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| users loads the application | *On page load* | user sees various photos posted on the application |
| user clicks on the photo | *On  click* | photo's details page is loaded showing the description, name , location and category |
| user searches for category on the search bar | *on page load* | different photos are loaded according to that category |
| user clicks on the loaction | *On page load* | different photos are loaded according to that location |
| user clicks on the copy button  |  | image link is copied to the clipboard |


## Prerequisites
* Python 3.8.10
* Django 3.2.10

## Setup/Installation Requirements
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/ian-otieno/Django-Gallery.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
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
python manage.py makemigrations pictures 
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
  
  
## Known Bugs

No known bugs

## Technologies Used
- Python3.8
- Django
- Heroku

## Contacts
Email: ian.otieno@student.moringaschool.com

 &#169; 2022 Ian Otieno
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
