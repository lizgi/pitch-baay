## pitch-bay

## Author
Elizabeth Gikonyo

## Description
Is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functions of the website,,.

## Live Link


## Screenshot


## User Story



## BDD
Behaviour	Input	Output
Load the page	On page load	Get all posts, Select between signup and login
Select SignUp	Email,Username,Password	Redirect to login
Select Login	Username and password	Redirect to page with app pitches based on categories and commenting section
Select comment button	Comment	Form that you input your comment
Click on submit		Redirect to all comments tamplate with your comment and other comments
Development Installation
To get the code..

## Cloning the repository:

https://github.com/lizgi/pitch-bay

Move to the folder and install requirements

cd pitch-bay

pip install -r requirements.txt

Exporting Configurations

export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

## Running the application

python3.8 manage.py server

running the test

python3.8 manage.py test

Open the application on your browser .

## Technology used

Python3.8

Flask

Heroku

## Known Bugs

There are no known bugs.

## Contact Information

If you have any question or contributions, please email me at []

## License
