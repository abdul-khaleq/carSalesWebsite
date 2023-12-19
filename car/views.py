from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from brand.models import BrandModel
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.CarModel
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_valid(form)

class CarDetailView(DetailView):
    model = models.CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car =self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        cars = models.CarModel.objects.all()
        context['cars'] = cars
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
def orderHistory(request, id):
    car = models.CarModel.objects.get(pk=id)
    if request.user:
        order_history = models.OrderHistoryModel(
            car_name=car.name,
            car_description=car.description,
            car_price=car.price,
            car_brand=car.brand,
            car_image=car.image,
            user=request.user,
        )
        if car.quantity >0:
            order_history.save()
            car.quantity -=1
            car.save()
        # car.delete()
    return redirect('homepage')

