from django.shortcuts import render

from item.models import Category, Item

# Create your views here.
# This info about the browser. If you gonna Post or Get
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')