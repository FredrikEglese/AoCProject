from django.urls import path
from . import views

app_name = 'AoC'

urlpatterns = [
    path('',                views.IndexView.as_view(), name = 'index'),
    path('solve/<str:question_id>/', views.SolveView.as_view(), name = 'solve'),
]
