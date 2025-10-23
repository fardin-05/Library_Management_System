from django.shortcuts import render
from rest_framework import viewsets
from .models import Author,Category,Book,Member,BorrowRecord
from .serializers import AuthorSerializer,CategorySerializer,BookSerializer,MemberSerializer,BorrowRecordSerializer
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
class BorrowRecordviewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
 
