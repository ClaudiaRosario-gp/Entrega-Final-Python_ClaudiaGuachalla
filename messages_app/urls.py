from django.urls import path
from . import views
from .views import conversation_detail

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('send/', views.send_message, name='send_message'),
    path('conversation/<str:username>/', conversation_detail, name='conversation_detail'),
]
