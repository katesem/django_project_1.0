from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about_page, name='about'),
    path('create_account', views.create_account, name='create_acc'),
    path('log_in', views.log_in, name = 'login')
]