from django.urls import path
from . import views

app_name = 'property'


urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('search/', views.property_search_list, name='property_search_list'),
    path('<int:id>/', views.property_detail, name='property_detail'),
    path('location/<int:location_id>/', views.property_location_total_detail, name='property_location_total_detail'),
]
