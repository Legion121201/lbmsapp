from rest_framework import serializers
from .models import Book, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'