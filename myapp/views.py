from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Employee, Item, Sale
from django.views.generic import View
from django.http import HttpResponseRedirect
import datetime
from .forms import LoginForm

class ItemListView(View):
    
    def get(self, request):

        items = Item.objects.all()
        context = {"items": items}
        return render(request, "item_list.html", context)

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