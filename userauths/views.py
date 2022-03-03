from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def home (request):
    return render(request, 'index.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')