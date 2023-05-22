# Description
The repository creates a discord like web app, FrontEnd (Html, CSS) , BackEnd (Django)

# python-web-app-development

The repo shows a simple discord like web app built with DJango Framework.


 1. Install Virtual env: ```pip install virtualenv```
 
 2. Name your virtaulenv : ```virtualenv env```

 3. Activate scripts: ```env/scripts/activate```

 4. Install django: ```pip install django```

 5. StartProject: ```django-admin startproject yourProjectNameHere```

 6. Start server : navigate to project folder  ```python manage.py runserver```

 7. move env folder into your project (copy-paste or just drag-drop) 

 8. Open the code in VS code

 9. If you see any error related to activation of scripts check this :  https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system

10. StartApp:  ```python manage.py startapp base``` (base is name of our app) - It will create a base folder containing essential files in our project

11. Tell django about our "base" app: Go to ```settings.py``` and add our base apps.py path

            INSTALLED_APPS : [
               'base.apps.BaseConfig'
            ]
            
12. Create a 'urls.py' fils inside 'base' app

13. create templates folder : add your htmls here

14. Let django know about this folder : Go to settings.py add the template folder 

15. Run migrations: python manage.py migrate

16. Make migration after every change in models  : ```python manage.py: makemigrations```

17. Migrate all changes  : ```python manage.py: migrate```

18: create a super user:  ```python manage.py createsuperuser ```


