from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AuthorViewSet,CategoryViewSet,BookViewSet,MemberViewSet,BorrowRecordviewSet


router = DefaultRouter()

router.register(r'author',AuthorViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'books',BookViewSet)
router.register(r'members',MemberViewSet)
router.register(r'borrow-record',BorrowRecordviewSet)

urlpatterns = [
    path('',include(router.urls))
]
