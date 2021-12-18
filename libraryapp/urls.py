from django.urls.conf import path
from django.conf.urls import url 
from django.urls import path
from libraryapp.views import UserView

urlpatterns = [
    path('users', UserView.as_view(), name='users')
]