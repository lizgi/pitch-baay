## pitch-bay

## Author
Elizabeth Gikonyo

## Description
Is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functions of the website,,.

## Live Link
pitchava.herokuapp.com/


## User Story
As a user, I would like to see the pitches other people have posted.

As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.

As a user, I would like to be signed in for me to leave a comment

As a user, I would like to view the pitches I have created in my profile page.

As a user, I would like to comment on the different pitches and leave feedback.

As a user, I would like to submit a pitch in any category.

As a user, I would like to view the different categories.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all posts, Select between signup and login on the right side|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | *Comment* | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

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
MIT License

Copyright (c) 2021 lizgi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
