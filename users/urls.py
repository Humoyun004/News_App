from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView

from .views import singUp, logOut, ProfileInfo

urlpatterns = [
    path('register/', singUp, name='singUp'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='Login'),
    path('logout/', logOut, name='logOut'),
    path('profile/', ProfileInfo, name='ProfileInfo'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/done.html'), name='password_reset_done'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users/complete.html', extra_context={'login_required': reverse_lazy('Login')}, http_method_names=['GET']), name='password_reset_complete')
]
