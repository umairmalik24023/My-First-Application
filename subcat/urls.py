
from django.urls import path
from django.urls import include, path
from .import views
urlpatterns = [
    
     path('panel/subcatagories/list/', views.Subcat_list, name='subcat_list'),
     path('panel/subcatagories/add/', views.Subcat_add, name='subcat_add'),
]

