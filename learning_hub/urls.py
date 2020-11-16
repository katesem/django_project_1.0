from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    #Common urls 
    path('', views.homepage, name='homepage'),
    path('about', views.about_page, name='about'),
    path('create_account', views.create_account, name='create_acc'),
    path('log_in', views.log_in, name = 'login'),
    path('log_out', views.log_out, name = 'logout'),
    path('my_account', views.my_account, name = 'my_account'),
    path('accounts/login/', views.password_redirect),
    path('contact', views.contact),
    
    #urls related to quiz creation 
    path('create_question', views.create_question, name = 'c_question'),
    path('create_quiz', views.create_quiz, name = 'c_quiz'),
    path('create_topic', views.create_topic, name = 'c_topic'),
    
    #urls related to topic display
    path('topic/<int:topic_id>', views.topic_by_id, name = 'get_topic_by_id'),
    path('all_topics', views.all_topics, name = "topics"),
    
    # urls related to quiz taking
    path('take_a_quiz/<int:quiz_id>', views.take_a_quiz, name = 'take_a_quiz'),
    path('quiz_results', views.quiz_results, name = 'quiz_results'),
    path('quiz_answers', views.quiz_answers, name = 'q_answers'),
    
    # Password reset functionality
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),  name="password_reset_done"),
    
     path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),  name="password_reset_confirm"), #user’s id encoded in base 64 and token to check that the password is valid.
     
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),  name="password_reset_complete"),
]