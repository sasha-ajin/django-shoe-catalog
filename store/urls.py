from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BrandList.as_view()),
    path('<str:brand>', views.LineList.as_view()),
    path('<str:brand>/<str:line>', views.ModelList.as_view())
]
