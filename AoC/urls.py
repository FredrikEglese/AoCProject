from django.urls import path
from . import views

app_name = 'AoC'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('solve/<str:question_id>/', views.solve, name = 'solve'),
]
