import pytest
import json
from django.urls import reverse
from api.domain.carnaval_domain import CarnavalDomain

def test_view_get_carnaval_year_even(client):
   param = 1986
   url = reverse('carnaval', args=(param,))
   response = client.get(url)
   assert response.status_code == 200

def test_view_get_carnaval_year_odd(client):
   param = 2019
   url = reverse('carnaval', args=(param,))
   response = client.get(url)
   assert response.status_code == 200

def test_view_year_invalid(client):
   param = 0
   url = reverse('carnaval', args=(param,))
   response = client.get(url)
   assert response.status_code == 400
