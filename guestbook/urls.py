from django.conf.urls.defaults import *
from Django_AppEngine import settings

import sys

import os.path, pkgutil

controllerPackage = __import__(settings.NAMESPACE + ".controllers", globals(), locals(), ['object'], -1) 

urlpatterns = patterns('')

pkgpath = os.path.dirname(controllerPackage.__file__)

controllers = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
controllers = filter(lambda x: x.endswith("Controller"), controllers)

map(__import__,  map(lambda c: settings.NAMESPACE + ".controllers." + c, controllers))

for controller in controllers:
    
    mod = dir(sys.modules[settings.NAMESPACE + ".controllers." + controller])
    actions = filter(lambda x: x.endswith("Action"), mod)
    for action in actions:
        
        actionRoute = '' if action == 'indexAction' else action[:-6]
        
        controllerRoute = '' if controller == 'HomeController' and action == 'indexAction' else controller[:-10] + '/'
        
        urlpatterns += patterns('',
            (r'^(?i)' + controllerRoute + actionRoute + '$', 'guestbook.controllers.' + controller + '.' + action),
        )