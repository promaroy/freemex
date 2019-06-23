[![GSoC Heat](https://img.shields.io/badge/GSoC%20Heat-2019-orange.svg)](https://nitdgpos.github.io/gsoc_heat)

# Freemex

**Freemex** is an online trading game which allows you to buy and sell stocks at your convenience and at the current market price. The player at the end with highest total stocks and cash wins the game.


## Building from Source

1. Create a **virtual environment** with virtualenv (install virtualenv, if its not installed).

    ```
    virtualenv freemex

    ```

2. Clone the project in the virtual environment directory.

    ```
    cd freemex
    git clone https://github.com/lugnitdgp/freemex.git

    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate

    ```

    #### For Windows
    ```
    .\Scripts\activate

    ```

4. Install the requirements.

    ```
    cd freemex
    pip install -r requirements.txt

    ```

5. Copy the .env.example file to .env file.

    ```
    cp .env.example .env

    ```

6. Open the .env file and add an arbitary secret key.

7. Generate Google+ OAuth credentials with the following steps:

    + Go to [Google developer console](https://console.developers.google.com/)    

    + Create a new project if you do not have any (see the drop-down at the top left of your screen).

    + After the project is created you will be redirected to a dashboard. Click on **ENABLE API** button.

    + Select **Google+** API from the Social APIs section.
    + On the next page, click the **Enable** button to enable Google+ API for your project.

    + To generate credentials, select the Credentials tab from the left navigation menu and hit the ‘Create Credentials’ button.

    + From the drop-down, select OAuth client ID.

    + On the next screen, select the application type (web application in this case) and enter your authorized javascript origins and redirect uri. For now, just set the origin as http://localhost:8000 and the redirect URI as http://localhost:8000/complete/google-oauth2/

    + Now, open the `.env` file and add your Google OAuth credentials.

8. Generate Facebook login credentials with the following steps:

    + Go to [Facebook Developers Console](https://developers.facebook.com/)

    + Click on **My Apps** and then **Add a New App**.

    + Enter _Display Name_ and _Contact Email_ and click on **Create App Id**.

    + Select **Facebook login** and choose **set up**. Pick **Web** on the next page.

    + Enter `http://localhost:8000` as the _Site Url_ and hit **Save**.

    + Now go to **Settings/Basic** and then in the _App Domains_ just put `localhost` and hit **Save Changes**.

    + Grab the App ID and App Secret and add them to the `.env` file.

9.  Migrate your database and run the Django Development Server.

    ```
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py runserver

    ```

10. Open `http://localhost:8000` in your browser. (Opening `http://127.0.0.1:8000` will cause problems with Social Login)

## Starting the game

1. Add the cronjob

    ```
    ./manage.py crontab add

    ```

2. Load the fixtures

    ```
    ./manage.py loaddata fixtures.json

    ```

3. Run the server and the prices should get updated every minute. Now, buy and sell stocks to make profit. Enjoy!

## For contributors

Freemex uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)

If you want to contribute to this project, then have a look [here](https://github.com/lugnitdgp/freemex/blob/master/CONTRIBUTING.md)
