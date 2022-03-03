from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/accounts/login/')
def home (request):
    return render(request, 'index.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')