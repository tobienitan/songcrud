from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('artiste/', views.ArtisteList.as_view()),
    path('artiste/<int:pk>/', views.ArtisteDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)