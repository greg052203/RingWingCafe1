from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm
from django.shortcuts import render


def home(request):
    return render(request, 'cafe/home.html')

def menu(request):
    return render(request, 'cafe/menu.html')

def order(request):
    return render(request, 'cafe/order.html')

def about(request):
    return render(request, 'cafe/about.html')

def contact(request):
    return render(request, 'cafe/contact.html')


def order(request):
    orders = Order.objects.all()  # Fetch all orders
    return render(request, 'cafe/order.html', {'orders': orders})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'cafe/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total = order.quantity * order.price
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'cafe/order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.total = order.quantity * order.price
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'cafe/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'cafe/order_confirm_delete.html', {'order': order})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = OrderForm()
    return render(request, 'cafe/create_order.html', {'form': form})

