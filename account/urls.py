from django.urls import path

from .views import *

urlpatterns = [
    #Leave as empty string for base url
	path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
