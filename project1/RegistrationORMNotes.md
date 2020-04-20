Task-1: Creating database table.
By using SQL Alchemy created a users database table with the table name as tables.py and with the fields username and password.
Initaialized the constructor for variables username and password. Assigned username with primary key because it to be unique and password with nullable to enter the values.
created configuration session and set up the database.
While running the flask I got some errors and then I debuged it..
After running the flask,while I was creating a dataclip in heroku,I got some issue when I selected the table.
I have fixed that bug by changing the tablename.I have done this by taking the reference from NGLMS video and tutorilspoint.
reference: https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
           https://www.youtube.com/watch?v=24Kf3v7kZyE
Time taken to complete this task is 2 hrs.

Task-2 : Inserting the records.
Added alerts with close button in registration form for registration status.
In database.py I have created two messages one is for error message if the user is already exist, another message is for successful registration.
I have objects in registration form and assigned to database.py file.
I faced a problem with alert close button then when I cross checked I didnt used the script by adding that the close button was worked.
reference: https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
           https://www.w3schools.com/bootstrap4/bootstrap_alerts.asp
Time taken to complete this task 1 hr.

Task-3 : Retrieving data from database table
Here I have created admin page using administration.html file in templates folder.
In this file I have listed the users in the order of creation timestamp.
Here I have displayed the Username password and there timestamp ina admininstration page.
First I had a problem in craeting the toimestamp column as I have choosed it null the time was not displayed again.
I debug the error by clicking on adminer and I have droped the table and made the changes in tables.py.
Reference: https://www.youtube.com/watch?v=24Kf3v7kZyE
Time taken to complete this task is 1 hr.
