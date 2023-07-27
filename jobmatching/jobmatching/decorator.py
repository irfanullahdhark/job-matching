from django.http import HttpResponse
from django.shortcuts import redirect


def un_authentication(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.username.is_authenticated:
            return redirect('jobportal/index')
        else
        return view_func(request,*args,**kwargs)