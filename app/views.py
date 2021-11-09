"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import PurchaseForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Полезные ссылки.',
            'year':datetime.now().year,
        }
    )

def purchase(request):
  assert isinstance(request, HttpRequest)
  data = None
  paymentMethod = {'1': 'Картой на сайте','2': 'Картой курьеру','3': 'Наличными руьеру'}
  if request.method == 'POST':
    form = PurchaseForm(request.POST)
    if form.is_valid():
      data = dict()
      data['name'] = form.cleaned_data['name']
      data['address'] = form.cleaned_data['address']
      data['phone'] = form.cleaned_data['phone']
      data['email'] = form.cleaned_data['email']
      data['paymentMethod'] = form.cleaned_data['paymentMethod']
      data['agreement'] = form.cleaned_data['agreement']
      form = None
  else:
    form = PurchaseForm()
  return render(
        request,
        'app/purchaseForm.html',
        {
          'title':'Оплата',
          'form':form,
          'data':data,
          'year':datetime.now().year,
        }
    )
