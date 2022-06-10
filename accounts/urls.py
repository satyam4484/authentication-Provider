from urllib.parse import urlparse
from django.urls import path 
from .views import userDetails,createUser
urlpatterns = [
    path('',userDetails),
    path('signup/',createUser)
]
