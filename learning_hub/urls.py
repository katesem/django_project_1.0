from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about_page, name='about'),
    #path('sign_up', views.sign_up,name='sign_up')
]