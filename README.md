# beChallenge_solution

Hi! Look at one way to solve the Be Challenge which is proposed in https://gist.github.com/scabbiaza/82e9069cfa71c4d7aa9d9539a794a1db

Let´s look its functionality.	
# Structure
The project is done with flask for the API develop and with peewee for the SQLite database model and connection. All the infrastructe are integrated in a docker container and for your access this project is deployed in Heroku.
# How to test

Currently, the API let you access to the users information by the endpoint URL:

    https://be-challenge-kvivanco.herokuapp.com/bechanllengeapi/user/<username>/<pagenumber>

The API let you search an user from the DB by changing *username* in the endpoint with the user username that you want to retrieve, i.e.

    https://be-challenge-kvivanco.herokuapp.com/bechanllengeapi/user/shawricardo

Also, you can retrieve users by filtering their username, by sending as param the letters that filter them, i.e. If you wanna filter all users which username contains "ca", the URL may be:

    https://be-challenge-kvivanco.herokuapp.com/bechanllengeapi/user/ca

You can see just ten users per page, so if you wanna see other users, try paging the results changing the *pagenumber*  parameter with a specific page, i.e.

        https://be-challenge-kvivanco.herokuapp.com/bechanllengeapi/user/ca/8

As you can see the number *8* is the page you want to see the results. If you don't send a specific *pagenumber* the API take by default the number ***1***.

## Replicate and test project locally

***The project is build under python 3.9***

Once you have cloned the repository, you can install all the dependencies by running the command 

    pip3 install -r requirements.txt 
Initially, the users database has 1MM users but if you prefer delete the current DB and create another one, you can execute the *generate_users.py* file that generates randomly 1MM users with the fields defined in the *models.py* file.

- To test the project locally, please change the port defined in the *main.py* file with ***9200***.

*Not to forget to add the new libraries to the requirements.txt file, that you added in the project, with the command*

    pip3 freeze >> requirements.txt

To sun the project with docker it´s necesary save the previous changes by running the command.

    docker build -t be-challenge-app .

And, after that run:

    docker run -p 8080:9200 -it --rm --name be-challenge-container-app be-challenge-app
Now, you can access to the users information by using the same URI defined in the last section by changing the base path *https://be-challenge-kvivanco.herokuapp.com/* with *localhost:8080*