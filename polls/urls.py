from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('<int:question_id>/', detail, name="detail"),
    path('<int:question_id>/result', result, name="result"),
]