from rest_framework import serializers
from .models import *
import re


class PhoneBookSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PhoneBook
        fields = ["id","description"]

    def create(self, validated_data):
        user = self.context.get('request').user
        newPhoneBook = PhoneBook(user = user,**validated_data)
        newPhoneBook.save()
        return newPhoneBook


class TagSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Tag
        fields = ["tag_name"]


class PhoneNumberSrializer(serializers.ModelSerializer):
    phone_number  = serializers.CharField(
        label="phone_number",
        required=True
    )
    tag = TagSerializer()

    class Meta(object):
        model = PhoneNumber
        fields = [
            "id",
            "phone_number",
            "tag"
        ]

    def validate_phone_number(self, value):
        if PhoneNumber.objects.filter(contact__id=self.context.get('view').kwargs.get('contact_pk'), phone_number = value).exists():
            raise serializers.ValidationError("Phone number already exists.")
        if not re.match(value, r'^\+?1?\d{9,15}$'):
            raise serializers.ValidationError("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        return value
    
    def create(self, validated_data):
        contact = self.context.get('view').kwargs.get('contact_pk')
        tagName = validated_data.pop('tag')
        numberTag, created = Tag.objects.get_or_create(tag_name = tagName)
        newNumber = PhoneNumber(tag = numberTag,**validated_data)
        newNumber.save()
        Contact.objects.get(id = contact).numbers_list.add(newNumber)
        phone_number.save()
        return phone_number

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'tag':
                tagName, created = Tag.objects.get_or_create(tag_name = value)
                instance.tag = tagName
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class ContactSerializer(serializers.ModelSerializer):
    numbers_list = PhoneNumberSrializer(many = True)

    def validation(self, attrs):
        if not (attrs['first_name'] or attrs['last_name'] or attrs['nick_name']):
            raise serializers.ValidationError("Either first name or first name or nick name must be provided")
        return attrs

    class Meta(object):
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "nick_name",
            'numbers_list'
        ]

    def create(self, validated_data, *args, **kwargs):
        contactPhonebookId = self.context.get('view').kwargs.get('phonebook_pk')
        contactPhonebook = PhoneBook.objects.get(id = contactPhonebookId)
        numbersList = validated_data.pop('numbers_list')
        numbersList.save()
        contactObject = Contact(phone_book = contactPhonebook,**validated_data)
        numbersObjects = []
        for newNumber in numbersList:
            tagName = newNumber.pop('tag')
            numberTag, created = Tag.objects.get_or_create(tag_name = tagName)
            newNumber = PhoneNumber(tag = numberTag, phone_number = newNumber['phone_number'])
            newNumber.save()
            numbersObjects.append(newNumber)
        contactObject.numbers_list.add(*numbersObjects)
        contactObject.save()
        return contactObject



