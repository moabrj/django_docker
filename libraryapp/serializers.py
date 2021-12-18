from rest_framework import serializers
from libraryapp.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'cpf', 'phone', 'email', 'addressStreet',
            'addressNumber', 'addressCity', 'addressState', 'password')