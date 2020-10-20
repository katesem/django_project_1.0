from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about_page, name='about'),
    path('create_account', views.create_account, name='create_acc'),
    path('log_in', views.log_in, name = 'login'),
    path('log_out', views.log_out, name = 'logout'),
    path('my_account', views.my_account, name = 'my_account')
]