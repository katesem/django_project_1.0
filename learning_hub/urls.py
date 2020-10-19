from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('sign_up', views.sign_up,name='sign_up')
]