from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def books(request):
  mybooks = Book.objects.all().values()
  template = loader.get_template('all_books.html')
  context = {
    'mybooks': mybooks,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mybook = Book.objects.get(id=id)
  template = loader.get_template('book_details.html')
  context = {
    'mybook': mybook,
  }
  return HttpResponse(template.render(context, request))

###########
def main(request):
  book1 = Book.objects.get(bookname="統計學：以 Microsoft Excel 為例（第九版）")
  book2 = Book.objects.get(bookname="系統程式設計(上册)")
  book3 = Book.objects.get(bookname="來自深淵(05)")
  book4 = Book.objects.get(bookname="天龍八部(一)新修版")
  book5 = Book.objects.get(bookname="魔戒前傳：哈比人歷險記")
  book6 = Book.objects.get(bookname="麥田捕手")
  book7 = Book.objects.get(bookname="戰爭與和平")
  book8 = Book.objects.get(bookname="殺死一只知更鳥")
  
  template = loader.get_template('main.html')
  context = {
    'book1': book1,
    'book2': book2,
    'book3': book3,
    'book4': book4,
    'book5': book5,
    'book6': book6,
    'book7': book7,
    'book8': book8,
    
  }
  return HttpResponse(template.render(context))


@login_required

def borrow(request):
  if request.method == 'POST':
    isbn = request.POST.get('ISBN', '')

    try:
      book = Book.objects.get(ISBN=isbn)
      b_title = book.bookname

      if book.lastQuantity > 0:
        book.lastQuantity -= 1 #書籍數目-1
        book.save() #更新資料庫

        message = f'已借出《{b_title}》'
        return render(request, 'borrow.html', {'success': message})
      else:
        return render(request, 'borrow.html', {'error': '架上數量不足'})

    except Book.DoesNotExist:
      return render(request, 'borrow.html', {'error': '書籍不存在'})

  return render(request,'borrow.html')



@login_required
def return_book(request):
  if request.method == 'POST':
    isbn = request.POST.get('ISBN', '')

    try:
      book = Book.objects.get(ISBN=isbn)
      b_title = book.bookname

      if book.lastQuantity < book.maxQuantity:
        book.lastQuantity += 1 #書籍數目+1
        book.save() #更新資料庫

        message = f'已歸還《{b_title}》'
        return render(request, 'return_book.html', {'success': message})
      

      else: #書籍無借出
         return render(request, 'return_book.html', {'error': '書籍已全數歸還'})

    except Book.DoesNotExist:
      return render(request, 'return_book.html', {'error': '書籍不存在'})

  return render(request,'return_book.html')





