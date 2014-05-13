Django AppEngine Template
=========================

Template that incorporates Django with Google App Engine that is extended to make routing care free

Keep your application clean and organized!

Naming Conventions
---------
* Just add your controllers to the controllers package.  Use the suffic "Controller".
* Add your actions to your controller.  Actions have an "Action" suffix.


Set up the template for use with your project
--------
 - rename the 'guestbook' folder/package to the namespace you intend to use
 - in Django_AppEngine/settings.py update the NAMESPACE variable to match your namesapce
 - in Django_AppEngine/urls.py update the included pattern to reflect your namespace
 - in app.yaml update the application property to match the name of your App Engine application name
 


This template is based of this [this tutorial]

[this tutorial]:http://django-appengine.com/
