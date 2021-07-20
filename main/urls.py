from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login_data',views.login_credentials,name='login_data')
]
