from .models import ContactMe
from rest_framework import serializers



class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = ['email_address','message']


