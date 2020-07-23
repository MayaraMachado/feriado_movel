from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from api.domain.carnaval_domain import CarnavalDomain
from .serializers import CarnavalSerializer

class CarnavalView(APIView):

    def get(self, request, ano):  
        try:
            carnaval_domain = CarnavalDomain()
            data_carnaval = carnaval_domain.calcular(ano)
            response = CarnavalSerializer({"feriado":"Carnaval", "data":data_carnaval})
            return Response(response.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"message" : 'Ano inválido.'},status=status.HTTP_400_BAD_REQUEST)