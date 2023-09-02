from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SciFiBookList(generics.ListAPIView):
    queryset = Book.objects.filter(category='Sci-Fi')
    serializer_class = BookSerializer

class FictionBookList(generics.ListAPIView):
    queryset = Book.objects.filter(category='Fiction')
    serializer_class = BookSerializer

class ComedyBookList(generics.ListAPIView):
    queryset = Book.objects.filter(category='Comedy')
    serializer_class = BookSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

