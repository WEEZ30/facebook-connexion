from django.urls import path

from . import views

app_name = 'home'
# Create your tests here.
urlpatterns =[
 path('', views.login, name='login')
]
