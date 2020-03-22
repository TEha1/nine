from django.urls import path
from .views import CountryListView, CategoryListView, CountryRUView, CategoryRUView,\
    AdsCreateListView, AdsSearchListView, AdsRUView


urlpatterns = [
    path('countries/', CountryListView.as_view(), name="view all countries"),
    path('categories/', CategoryListView.as_view(), name="view all categories"),
    path('ads/', AdsCreateListView.as_view(), name="add and view ads"),
    path('ad/title/<str:title>/', AdsSearchListView.as_view(), name="ads search by category"),
    path('ad/<int:pk>/', AdsRUView.as_view(), name="get specific store"),
    path('country/<int:pk>/', CountryRUView.as_view(), name="get specific country"),
    path('category/<int:pk>/', CategoryRUView.as_view(), name="get specific country"),
]
