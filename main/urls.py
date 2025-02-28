from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topic_list, name='topic'),
    path('contact/', views.contact, name='contact'),
    path('topics/<int:pk>/', views.topic_detail, name='topic-detail'),
    path('solution/<int:pk>', views.solution, name='solution')
]
