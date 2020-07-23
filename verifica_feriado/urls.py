from django.contrib import admin
from django.urls import path
from api.application.views import CarnavalView

urlpatterns = [
    path('carnaval/<int:ano>', CarnavalView.as_view(), name='carnaval'),
]
