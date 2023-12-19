from django.shortcuts import render
from car. models import CarModel
from brand.models import BrandModel

def home(request, id = None):
    cars = CarModel.objects.all()
    if id is not None:
        brand = BrandModel.objects.get(id=id)
        cars =CarModel.objects.filter(brand=brand)
    brands = BrandModel.objects.all()
    return render(request, 'home.html', {'cars':cars, 'brands':brands})