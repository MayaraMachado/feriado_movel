from rest_framework import serializers

class CarnavalSerializer(serializers.Serializer):
    feriado      = serializers.CharField()
    data = serializers.DateField()