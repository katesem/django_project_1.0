from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about_page, name='about'),
    path('create_account', views.create_account, name='create_acc'),
    path('log_in', views.log_in, name = 'login'),
    path('log_out', views.log_out, name = 'logout'),
    path('my_account', views.my_account, name = 'my_account'),
    path('accounts/login/', views.password_redirect),
    
    path('create_question', views.create_question, name = 'c_question'),
    path('create_quiz', views.create_quiz, name = 'c_quiz'),
    
    
    # Password reset functionality
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),  name="password_reset_done"),
    
     path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),  name="password_reset_confirm"), #user’s id encoded in base 64 and token to check that the password is valid.
     
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),  name="password_reset_complete"),
]