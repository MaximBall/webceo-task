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


@receiver(post_save, sender = Item)
def change_price_item(instance, **kwargs):
    
    new_change_price = ChangePrice(
        item = instance,
        date_change = datetime.datetime.now(),
        price = instance.price
    )
    new_change_price.save()


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

class BuyView(View):

    def get(self, request, name):

        items = Item.objects.filter(name=name)
        context = {"items": items, "name": name}
        return render(request, "buy_item.html", context)
        

    def post(self, request, name):
        
        count = int(request.POST.get("count_item"))
        select_dropdown = request.POST.get("dropdown")
        list_data = select_dropdown.split()

        user = User.objects.get(username=list_data[0])
        employe = Employee.objects.get(user=user)
        item = Item.objects.get(name=name, employe=employe, price=list_data[1])

        total_price = count * item.price

        new_sale = Sale(
            item=item,
            employe=employe,
            count=count,
            total_price=total_price,
            price_one_item=item.price,
            date_sale=datetime.datetime.now()
        )

        new_sale.save()
        route = "/"
        return HttpResponseRedirect(route)


class LoginView(View):

    def get(self, request):
        try:
            del request.session["data"]  
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
                request.session["data"] = user.username
                return HttpResponseRedirect("/")
        return render(request, "login.html", {"form": form})


