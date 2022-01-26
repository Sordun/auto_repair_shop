from rest_framework import serializers

from shop.models import Clients, Specialist, CheckIn


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ["url", "name", "user", "car_model"]


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ["url", "specialist_name"]


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ["url", "name", "specialist", "date", "time"]
