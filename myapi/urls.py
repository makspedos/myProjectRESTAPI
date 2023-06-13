from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.DataResponse.as_view()),
    path('<int:pk>/', views.DataResponse.as_view()),
    path('parse-json', views.simpleParse),
]

urlpatterns = format_suffix_patterns(urlpatterns)