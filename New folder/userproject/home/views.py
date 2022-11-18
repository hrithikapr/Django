from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pswd = request.POST.get('password')
        # ----- check whether user has input correct credentials ------
        user = authenticate(username=user, password=pswd)
        if user is not None:
            # ----- if Authenticated the credentials -----
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")