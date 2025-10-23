from django.contrib import admin
from .models import Author,Book,Category,Member,BorrowRecord
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','biography']
    list_filter = ['id','name']
    search_fields = ['id','name']
@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
    list_display = ['id','name','title','isbn','category','author','is_available']
    list_filter = ['id','name','isbn','author']
    search_fields = ['id','name','isbn','author__name']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','membership_status']
    list_filter = ['id','name']
    search_fields = ['id','name']
@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['id','book','member','borrow_date','delivery_date','return_date','status']
    list_filter = ['id','book','member']
    search_fields = ['id','book__name','member__name']