from django.urls import path
from .views import *

urlpatterns = [
    path('new_about/<int:new_about>/',new_about,name='new_about'),
    path('categories/<int:category_id>/',categories,name='categories'),
    path('index/',index),
]
