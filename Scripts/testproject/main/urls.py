from django.urls import path

from .views import index
from .views import show_search,SearchResultsView

app_name='main'
urlpatterns=[
    path('search_client/',show_search,name='show_search'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('',index,name='index'),
]