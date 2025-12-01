from django.shortcuts import render
from rest_framework import viewsets
from .models import Author,Category,Book,Member,BorrowRecord
from .serializers import AuthorSerializer,CategorySerializer,BookSerializer,MemberSerializer,BorrowRecordSerializer
#============Author Viewset=============
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#=============Category Viewset============
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#===============Book Viewset===============
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#================Member viewset=============
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

#================BorrowRecord Viewset============
class BorrowRecordviewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
 
