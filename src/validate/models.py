from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Code(models.Model):
    code=models.CharField('code',max_length=30,blank=True)
    
    def __unicode__(self):
        return self.code or 'uncode'

class Mac(models.Model):
    mac=models.CharField('mac',max_length=100,blank=True)
    code=models.OneToOneField(Code,verbose_name='code',blank=True,null=True)
    start_time=models.DateTimeField(verbose_name='start time',auto_now_add=True)
    last_time=models.DateTimeField(verbose_name='last time',auto_now=True)
    
    def __unicode__(self):
        return self.mac