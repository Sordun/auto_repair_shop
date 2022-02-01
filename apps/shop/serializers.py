from rest_framework import serializers

from shop.models import Client, Specialist, CheckIn


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name", "user", "car_model"]


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ["name"]


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ["name", "specialist", "date", "time"]
