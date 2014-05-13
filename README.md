Django_AppEngine_Template
=========================

Template that incorporates Django with Google App Engine that is extended to make routing care free

Just add your controllers to the controllers package.  Use the suffic "Controller".
Add your actions to your controller.  Actions have an "Action" suffix.

 - rename the 'guestbook' folder/package to the namespace you intend to use
 - in Django_AppEngine.settings update the NAMESPACE variable to match your namesapce
 - in app.yaml update the application property to match the name of your App Engine application name
 
 Keep your application clean and organized!