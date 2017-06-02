from base import *

from helpers.maintenance.log import log_setting

log_setting.SET(globals())

DATABASES = {
    'default': {
        'NAME': 'wxpush',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'he123811',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }