from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)
    else:
        products = Product.objects.all()

    # pagination
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html', {'products': products})

def detail(request, item_id):
    product = Product.objects.get(pk=item_id)
    return render(request, 'shop/detail.html', {'product': product})

def checkout(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        items = request.POST['placeOrder']

        order = Order(name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, items=items)
        order.save()
    return render(request, 'shop/checkout.html')