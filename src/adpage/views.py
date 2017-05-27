from django.shortcuts import render

# Create your views here.
def commonpage(request,name=''):
    if not name:
        name='home'
    temp = 'adpage/%s.html'%name
    return render(request,temp)