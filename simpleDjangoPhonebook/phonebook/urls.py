from django.urls import re_path ,path
from django.conf.urls import url
from .viewsets import *
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers




urlpatterns = [
    path('v1/phonebooks/', phonebook_list, name='phonebooks-list'),
    path('v1/phonebooks/<int:pk>/', phonebook_detail, name='phonebook-detail'),
    path('v1/phonebooks/<int:phonebook_pk>/contacts/', contact_list, name='contacts-list'),
    path('v1/phonebooks/<int:phonebook_pk>/contacts/<int:pk>/', contact_detail, name='contacts-detail'),
    path('v1/phonebooks/<int:phonebook_pk>/contacts/<int:contact_pk>/phonenumbers/',phonenumber_list, name='phonenumber-list'),
    path('v1/phonenumbers/<int:pk>/', phonenumber_detail, name='phonenumber-detail')
]