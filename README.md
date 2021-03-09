# Ecommerce
PART-1: Configure App
  In this section we will take care of getting our project set up. We'll first install Django and handle basic configuration.
  
  STEP1--Assuming you have Python installed, open up your command prompt and Pip install Django if you have not already done so.
  
  STEP2--Let's create our project. CD into where you want your project files.
       --We will use django-admin startproject “project name”.
       --Once you create your project be sure to CD into it before the next step.
  
  STEP3--Create the first app files with python manage.py startapp “appname". 
  
  STEP4--When you open up your project you should see the app we just created in your project folder. Make sure you add the new app to INSTALLED_APPS within settings.py.
  
  STEP5--In your command promt run "python manage.py runnserver" and open up port 127.0.0.1:8000. If everything was done correctly, you should see the default Django landing page.

