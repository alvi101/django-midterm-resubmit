from django.urls import path
from . import views

urlpatterns = [
    path("detail/<int:pk>/", views.CarDetail.as_view(), name='detail'),
    path("buy/<int:id>/", views.buy, name='buy'),
]
