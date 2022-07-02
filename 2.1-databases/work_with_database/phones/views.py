from django.shortcuts import render, redirect
from .models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort == 'name':
        all_phones = all_phones.order_by('name')
    elif sort == 'max_price':
        all_phones = all_phones.order_by('-price')
    elif sort == 'min_price':
        all_phones = all_phones.order_by('price')
    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    model = Phone.objects.get(slug__contains=slug)
    context = {'phone': model}
    return render(request, template, context)