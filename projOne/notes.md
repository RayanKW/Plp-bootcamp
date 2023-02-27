Step 1: make your folder. then cd into it.
step 2: make the virtual env i.e python -m venv <environmentName>
step 3: activate the env i.e source ./bin/ activate
step 4: pip install django
step 5: the django-admin statapp AppName . then code .
step 6: make the Apps related to you AppName  i.e python manage.py startapp appName
step 7: register the app in the settings.py of AppName.
step 8: create your models in appName and remember after to import them in the admin.py of the appName
step9:  make migrations i.e python manage.py makemigrations then python manage.py migrate.
