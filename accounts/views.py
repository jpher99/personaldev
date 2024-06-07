from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter

@login_required
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Approved').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 
               'customers':customers,
               'total_customers':total_customers,
               'total_orders':total_orders,
               'delivered':delivered,
               'pending':pending,}
    return render(request, 'accounts/dashboard.html', context)


@staff_member_required
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/create_user.html', context)


def items(request):
    items = Item.objects.all()

    return render(request, 'accounts/products.html', {'items': items})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer,
               'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter,
               }
    return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('item_name', 'status'), extra=1)
    formset = OrderFormSet(instance=customer)
    
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method == 'POST':
        form= OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,
               
               }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)