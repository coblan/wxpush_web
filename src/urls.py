"""wxpush_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from validate import views as validate_views
from adpage import views as adpage_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wx/?$',validate_views.valide),
    url(r'^bj/?$',validate_views.set_code),
    url(r'^$',adpage_views.commonpage),
    url(r'^web/(?P<name>\w+)/?$',adpage_views.commonpage),
]


#from django.conf import settings
#from django.conf.urls.static import static

#if settings.DEBUG:
    #urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)