# User Authentication
This project consist of User authentication and authorization consists of User signup , sign in, logout, forget password, update password, profile update using django.

# Technology Stack
- Python 3.5.2
- Django
- MySQL Database

# Project Structure
__user_authentication_project__<br/>
|--__templates__<br />
&nbsp; &nbsp;|--base.html<br />
&nbsp; &nbsp;|--index.html<br />
&nbsp; &nbsp;|--__account__<br />
&nbsp; &nbsp; &nbsp; &nbsp;  |--change_password.html<br />
&nbsp; &nbsp;  &nbsp; &nbsp; |--forget_password.html<br />
&nbsp; &nbsp; &nbsp; &nbsp;  |--login.html<br />
&nbsp; &nbsp;&nbsp; &nbsp;   |--password_reset_complete.html<br />
&nbsp; &nbsp; &nbsp; &nbsp;  |--password_reset_confirm.html<br />
&nbsp; &nbsp; &nbsp; &nbsp;  |--password_reset_done.html<br />
&nbsp; &nbsp; &nbsp; &nbsp;  |--profile_update.html<br />
&nbsp; &nbsp;  &nbsp; &nbsp; |--signup.html<br />
|--__user_authentication_project__<br />
&nbsp; &nbsp; |--migrations<br />
&nbsp; &nbsp; |--__pycache__<br />
&nbsp; &nbsp; |--admin.py<br />
&nbsp; &nbsp; |--apps.py<br />
&nbsp; &nbsp; |--forms.py<br />
&nbsp; &nbsp; |--__init__.py<br />
&nbsp; &nbsp; |--models.py<br />
&nbsp; &nbsp; |--tests.py<br />
&nbsp; &nbsp; |--urls.py<br />
&nbsp; &nbsp; |--views.py<br />
|--__user_authentication_project__<br />
&nbsp; &nbsp; |--__pycache__<br />
&nbsp; &nbsp; |--__init__.py<br />
&nbsp; &nbsp; |--settings.py<br />
&nbsp; &nbsp; |--urls.py<br />
&nbsp; &nbsp; |--wsgi.py<br />
|--manage.py<br />


#Running locally
-create a virtual environment.
-create a django project.
-clone the repo using git@github.com:paridhigoyal/User-Authentication.git
-pip install -r requirements/dev.txt
-python manage.py migrate
-python manage.py runserver.





