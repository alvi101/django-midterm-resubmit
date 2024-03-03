from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from car.models import Car
from brand.models import Brand


# def home(request):
#     return render(request, 'home.html')


class HomeView(ListView):
    template_name = 'home.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['cars'] = Car.objects.all()
        return context


def brand_filter(request, id):
    brand = Brand.objects.get(pk=id)
    cars = Car.objects.filter(brand=brand)
    brands = Brand.objects.all()
    return render(request, 'brand_filter.html', {'cars': cars, 'brands': brands})
