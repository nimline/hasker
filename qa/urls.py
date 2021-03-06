from django.urls import path, include

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ask/', views.AskView.as_view(), name='ask_view'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/signup/', views.signup, name='signup'),
    path('<int:pk>/', views.QuestionView.as_view(), name='question_view'),
    path('<int:question_id>/answer', views.answer_question, name='answer_question'),
    path('<int:question_id>/vote', views.question_vote, name='question_vote'),
]
