# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpResponse
import base64
from .models import Code,Mac
from django.utils import timezone
import json
# Create your views here.

"""
wx 代表 mac 地址
bj 代表 CD KEY

"""

def valide(request):
    mac_str=request.GET.get('wx')
    if not mac_str:
        return  HttpResponse({'status':'fail'},content_type="application/json")  
    
    mac_str = base64.b64decode(mac_str)
    mac,_ = Mac.objects.get_or_create(mac=mac_str)
    if mac.code:
        dc = {'status':'success'}
    else:
        now = timezone.now()
        delta = now-mac.start_time
        if delta.days >3 :
            dc={'status':'fail'}
        else:
            # 小于三天，试用期。
            dc={'status':'success','try_user':True}
    return HttpResponse(json.dumps(dc),content_type="application/json")  


def set_code(request):
    mac_str=request.GET.get('wx')
    mac_str = base64.b64decode(mac_str)  
    mac,_ = Mac.objects.get_or_create(mac=mac_str)
    
    code_str=request.GET.get('bj')
    code_str= base64.b64decode(code_str) 
    code=Code.objects.filter(code=code_str).first()
    
    if code and not getattr(code,'mac',None):
        mac.code=code
        mac.save()
        dc={'status':'success'}
    else:
        dc={'status':'fail','msg':'无效注册码'}
    return HttpResponse(json.dumps(dc),content_type="application/json")  