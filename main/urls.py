from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index_urls'),
    path('create-message/', create_message_view, name='create_message_urls')
]

