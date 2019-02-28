from django.urls import path
from . import views

app_name = 'property'


urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('search/', views.property_search_list, name='property_search_list'),
    path('<int:id>', views.property_detail, name='property_detail'),
]