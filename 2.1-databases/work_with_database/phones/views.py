from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get("sort", None)
    if sort:
        match sort:
            case "name":
                phones = phones.order_by("name")
            case "min_price":
                phones = phones.order_by("price")
            case "max_price":
                phones = phones.order_by("-price")
            case _:
                pass
    context = {
        "phones": phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, phoneModel=slug)
    context = {
        "phone": phone,
    }
    return render(request, template, context)
