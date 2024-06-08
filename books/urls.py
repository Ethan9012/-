from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    path('books/book_details/<int:id>', views.details, name='book_details'),
    path('borrow/', views.borrow, name='borrow'),
    
    path('return_book/', views.return_book, name='return_book'),
]
