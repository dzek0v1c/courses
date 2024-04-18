from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login as auth_login


def index(request):
    user = request.user
    return render(request, 'theme/index.html', {'user':user})
def auth(request):
    return render(request, 'login.html')
def profile(request):
    user = request.user
    return render(request, 'profile.html',)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return JsonResponse({"success": True, "message": "Registration successful"}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def login(request) :
    if request.method == 'POST':
        form = CustomAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=username, password=password)
            if user is not None:
                auth_login(request, user)
                return JsonResponse({"success": True, "message": "Login successful"}, status=200)
            else:
                return JsonResponse({"success": False, "message": "Invalid username or password"}, status=400)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors}, status=400)
    else:
        return JsonResponse({"success": False, "message": "Invalid request"}, status=400)
    
def course1(request):
    return render(request, 'course1.html')
def course2(request):
    return render(request, 'course2.html')
def course3(request):
    return render(request, 'course3.html')
def course4(request):
    return render(request, 'course4.html')
def course5(request):
    return render(request, 'course5.html')
def course6(request):
    return render(request, 'course6.html')
