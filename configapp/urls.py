from django.urls import path
from .views import *

urlpatterns = [
    path('new_about/<int:new_id>/', new_about, name='new_about'),
    path('category/<int:category_id>/', category_news, name='category_news'),  # Переименовали функцию
    path('index/', index, name='home'),
    path('news_add/',add_news, name='add_news'),
    path('add_categories/',add_categories, name='add_categories'),
]

