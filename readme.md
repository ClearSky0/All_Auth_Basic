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
6. start the site
7. test the site
8. make it yours

## Commands
My preferred commands for the above, run from the base project folder.

        python -m venv venv
        venv\Scripts\activate
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py runserver 0.0.0.0:8000

Then over to you.