from rest_framework import serializers
from .models import Contact
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username']

class ContactList(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Contact
		fields = '__all__'