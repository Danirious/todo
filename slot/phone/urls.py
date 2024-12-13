from . import views
from django.urls import path
app_name = 'phone'
urlpatterns = [
path('',views.index,name='index'),
path('simple/',views.simple,name='simple'),
path('complex/',views.complex,name='complex'),
]