from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.views.decorators.csrf import csrf_exempt


phonebook_list = PhoneBookView.as_view({
    'get': 'list',
    'post': 'create'
})
phonebook_detail = PhoneBookView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
contact_list = ContactsView.as_view({
    'get': 'list',
    'post': 'create'
})
contact_detail = ContactsView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

phonenumber_list = PhoneNumberViewList.as_view({
    'get': 'list',
    'post': 'create'
})

phonenumber_detail = PhoneNumberViewDetail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})