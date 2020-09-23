from django.urls import path
from . import views
from django.contrib.auth.views import(
    PasswordResetView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView
    )


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile_update', views.update_profile, name='profile_update'),
    path('forgot_password/', PasswordResetView.as_view(
        template_name='account/forgot_password.html'), name='forgot_password'),
    path('password_reset_done', PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', (
        PasswordResetConfirmView).as_view(
            template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),
    path('change_password', views.change_user_password,
         name='change_password'),
]
