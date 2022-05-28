from . import views
from django.urls import path


urlpatterns=[
    path('',views.home, name='landing'),
    path('search/', views.search_results, name='search_results')
]