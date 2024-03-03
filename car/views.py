from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Car
from comments.models import Comment
from comments.forms import CommentForm
from customers.models import PurchaseHistory

# Create your views here.


class CarDetail(DetailView):
    template_name = 'car_detail.html'
    model = Car
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(self.request.POST)
        current_car = self.get_object()
        print(current_car)
        if request.method == "POST":
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = current_car
                new_comment.name = request.user.username
                new_comment.save()
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_car = self.get_object()
        context['comments'] = Comment.objects.filter(car=current_car)
        context['comment_form'] = CommentForm()
        return context


"""
class PurchaseHistory(models.Model):
    car_image = models.ImageField()
    car_name = models.CharField(max_length=200)
    car_brand = models.CharField(max_length=200)
    price = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

"""


def buy(request, id):
    car = Car.objects.get(pk=id)
    new_history = PurchaseHistory(car_image=car.thumbnail, car_name=car.car_name,
                                  car_brand=car.brand.name, price=car.price, user=request.user)
    new_history.save()
    print(car.quantity)
    car.quantity = car.quantity - 1
    car.save()
    print(car.quantity)
    return redirect('profile')