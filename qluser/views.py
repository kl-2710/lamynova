from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'qluser/login.html', {'form': form})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'qluser/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Đăng ký thành công. Vui lòng tiếp tục đăng nhập để truy cập website.')
            return redirect('signup success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'qluser/signup.html', {'form': form}) 

def signup_success(request):
    return render(request, 'qluser/signup-success.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Bạn đã đăng xuất thành công.")
    return redirect(reverse('index'))