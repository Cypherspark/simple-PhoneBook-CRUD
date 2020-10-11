from rest_framework import viewsets
from rest_framework import generics, permissions, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import *
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class PhoneBookView(viewsets.ModelViewSet):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer
    permission_classes = [permissions.IsAuthenticated]

@method_decorator(csrf_exempt, name='dispatch')
class ContactsView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'nick_name', 'numbers_list__phone_number']
    ordering_fields = ['first_name', 'last_name', 'nick_name']

    def get_queryset(self):
        queryset = Contact.objects.filter(phone_book = self.kwargs['phonebook_pk'])
        return queryset

    
@method_decorator(csrf_exempt, name='dispatch')
class PhoneNumberViewList(viewsets.ModelViewSet):
    serializer_class = PhoneNumberSrializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        contactQuerySetId = Contact.objects.get(phonebook = self.kwargs['phonebook_pk']).id
        queryset = PhoneNumber.objects.filter(contacts__id = contactQuerySetId)
        return queryset

@method_decorator(csrf_exempt, name='dispatch')
class PhoneNumberViewDetail(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSrializer
    permission_classes = [permissions.IsAuthenticated]
    






    