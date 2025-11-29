from django.db import models
from django.utils import timezone
from datetime import timedelta

#==========Author Section=============
class Author (models.Model):
    name = models.CharField(max_length=20)
    biography = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    isbn =models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Member(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    membership_status = models.CharField(max_length=10, choices=[
        ('active','Active'),
        ('expired','Expired'),
        ('suspanded','Suspanded')
    ],
       default='active'                                    
    )
    def __str__(self):
        return self.name
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    member = models.ForeignKey(Member,on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date  = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=15,choices=[
        ('borrow','Borrow'),
        ('returned','Returned'),
        ('late','Late'),
    ],
    default='borrow'
    )
    def save(self,*args, **kwargs):
        if not self.delivery_date:
            self.delivery_date = (self.borrow_date+timedelta(days=30)).date()
        if timezone.now().date()>self.delivery_date:
            self.status = 'late'
        if self.status == 'borrow':
            self.book.is_available = False
        else :
            self.book.is_available = True
        self.book.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.book},{self.member.name},{self.borrow_date},{self.status}"
        

