from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomSetPasswordForm

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup-success/', views.signup_success, name='signup success'),
    path('logout/', views.logout_view, name='logout'),
    # Các URL đặt lại mật khẩu của Django
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='qluser/reset-password.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='qluser/password_reset_done.html'),
         name='password_reset_done'),
     path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
               template_name='qluser/password_reset_confirm.html',
               form_class=CustomSetPasswordForm 
          ),
          name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='qluser/password_reset_complete.html'),
         name='password_reset_complete'),
]