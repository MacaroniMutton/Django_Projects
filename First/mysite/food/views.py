from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm, SearchForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def home(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/home.html')
    context = {
        'items': item_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'food/index.html', context)

class HomeClassView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'food/index.html'

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html', context)

class DetailClassView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'food/detail.html'

def add_item(request):
    # if request.method == 'POST':
    #     form = ItemForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('food:home')
    # else:
    #     form = ItemForm(None)

    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.instance.user_name = request.user
        form.instance.item_name = form.instance.item_name.capitalize()
        obj = form.save()
        # return redirect('food:home')
        return redirect('food:detail', item_id=obj.id)
    context = {
        'form': form,
    }
    return render(request, 'food/item-form.html', context)

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form) 

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        # return redirect('food:home')
        return redirect('food:detail', item_id=item.id)
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:home')
    context = {
        'item': item,
    }
    return render(request, 'food/item-delete.html', context)

def delete_select(request):
    form = SearchForm(request.POST or None)
    item = 1
    if form.is_valid():
        item_name = form.cleaned_data.get('item_name')
        try:
            item = Item.objects.get(item_name=item_name.capitalize())
            return redirect('food:delete_item', item_id=item.id)
        except Item.DoesNotExist:
            item = None

            
    return render(request, 'food/search-form.html', {'form': form, 'exists': item})

def search(request):
    form = SearchForm(request.POST or None)
    item = 1
    if form.is_valid():
        item_name = form.cleaned_data.get('item_name')
        try:
            item = Item.objects.get(item_name=item_name.capitalize())
            return redirect('food:detail', item_id=item.id)
        except Item.DoesNotExist:
            item = None

            
    return render(request, 'food/search-form.html', {'form': form, 'exists': item})