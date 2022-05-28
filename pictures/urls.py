from . import views
from django.urls import path


urlpatterns=[
    path('',views.home, name='landing'),
    path('search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)