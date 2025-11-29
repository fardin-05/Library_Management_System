from rest_framework import serializers
from .models import Author,Category,Book,Member,BorrowRecord

#===========Author Serializer============
class AuthorSerializer (serializers.ModelSerializer):
    class Meta :
        model = Author
        fields = ['id','name','biography']

#===========Category Serializer===========
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

#============Book Serializer=============
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','title','isbn','category','author','is_available']

#============Member Serializer=============
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','name','email','membership_status']

#=============BorrowRecord Serializer============
class BorrowRecordSerializer(serializers.ModelSerializer):
    book_name = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)
    member_name = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all(),source='member', write_only=True)
    class Meta:
        model = BorrowRecord
        fields = ['id','book_name','member_name','borrow_date','delivery_date','return_date','status']
