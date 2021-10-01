from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Employee, Item, Sale, ChangePrice
from django.views.generic import View
from django.http import HttpResponseRedirect
import datetime
from .forms import LoginForm
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.views.generic.edit import CreateView



@receiver(post_save, sender = Item)
def change_price_item(instance, **kwargs):
    ChangePrice.objects.create(
        item = instance,
        date_change = datetime.datetime.now(),
        price = instance.price
    )


class ItemListView(View):
    
    def get(self, request):

        items = Item.objects.all()
        context = {"items": items}
        return render(request, "item_list.html", context)

class SaleListView(View):
    
    def get(self, request):

        sales = Sale.objects.order_by('-date_sale')

        sales_paginator = Paginator(sales, 5)

        page_num = request.GET.get('page')

        page = sales_paginator.get_page(page_num)

        context = {"page": page}
        return render(request, "sales_list.html", context)

class BuyViewCreate(CreateView):
    model = Sale
    template_name = 'buy_item.html'
    fields = ['item', 'count']


class LoginView(View):

    def get(self, request):
        try:
            logout(request)
            form = LoginForm(request.POST or None)
            context = {"form": form}
            return render(request, "login.html", context)
        except KeyError:
            form = LoginForm(request.POST or None)
            context = {"form": form}
            return render(request, "login.html", context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
        return render(request, "login.html", {"form": form})

class HistoryPriceView(View):
    
    def get(self, request):

        history_price = ChangePrice.objects.all()
        context = {"prices": history_price}
        return render(request, "history_price.html", context)