# Instagram-clone
Instagram clone where user can sign-up,login,view posts


![image](https://user-images.githubusercontent.com/57414671/172957509-6318ad7e-634e-4dfa-b2df-c07959390b79.png)

## Description

As a user of the application I should be able to:

* Sign up and login
* Add a post and caption
* Like a post
* Comment on a post
* Logout


### Prerequisites

# Setup and Installation  

  
#### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Instagram-clone.git
```
#### Navigate into the folder and install requirements  
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
python manage.py makemigrations art
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
 python manage.py runserver 
```
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 python manage.py runserver 9000
```
##### Testing the application  
 ```bash 
 python manage.py test app
```

  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  


## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

