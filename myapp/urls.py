
from django.urls import path
from django.urls import include, path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.admin_panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('register/', views.myregister, name='myregister'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/settings', views.site_settings, name='site_settings'),
    path('panel/about/settings', views.about_settings, name='about_settings'),
    path('panel/change/pass/', views.change_pass, name='change_pass'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    