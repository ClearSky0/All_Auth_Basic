# A Basic Working AllAuth Site
This is a working Django project with a fully working set of AllAuth pages.

It features single homepage with a menu bar with the links that show on the index.html.

## Next Steps
Once you've cloned the repo into your own project folder
1. create a virtual env
2. activate it
3. install the required packages
4. migrate the database
5. create a superuser
6. rename ".env update and rename to .env" to .env
7. generate a secret key
8. edit the .env file and put the secret key in and the email server details if required
9. start the site.  For some weird reason it won't read .env if run from the shell with _python manage.py runserver 0.0.0.0:8000_, so just run it in vsCode.
10. test the site
11. make it yours

## Commands
My preferred Powershell commands for the above, run from the base project folder.

        python -m venv venv
        venv\Scripts\activate
        python.exe -m pip install --upgrade pip
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py createsuperuser
        mv '.\.env update and rename to .env' .env
        python -c "import secrets; print(secrets.token_urlsafe())"

Edit the .env file and add the secret key output above, then run from vsCode.

Then over to you.