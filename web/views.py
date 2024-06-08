from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from books.models import Book

from web.forms import LoginForm

def login(request):
    ''' 登入 '''
    login_page = loader.get_template('login.html')
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            'user': request.user,
            'login_form': login_form,
        }
        return HttpResponse(login_page.render(context, request))
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                main_page = loader.get_template('main.html')
                context = {'user': request.user,
                           'message': '登入成功'}
            else:
                login_form = LoginForm()
                context = {
                    'user': request.user,
                    'login_form': login_form,
                    'message': '使用者名稱或密碼錯誤'
                }
            return HttpResponse(login_page.render(context, request))

        else:                    
            print ('Login error (login form is not valid)')
    else:
        print ('Error on request (not GET/POST)')





#############
def logout(request):
    ''' 登出 '''
    auth.logout(request)
    book1 = Book.objects.get(bookname="統計學：以 Microsoft Excel 為例（第九版）")
    book2 = Book.objects.get(bookname="系統程式設計(上册)")
    book3 = Book.objects.get(bookname="來自深淵(05)")
    book4 = Book.objects.get(bookname="天龍八部(一)新修版")
    template = loader.get_template('main.html')
    context = {
        'book1': book1,
        'book2': book2,
        'book3': book3,
        'book4': book4,
        
    }
    return HttpResponse(main_html.render(context, request))







