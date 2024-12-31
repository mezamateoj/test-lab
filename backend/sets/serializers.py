from rest_framework import serializers
from sets import models

class SetsSetializer(serializers.ModelSerializer):

    class Meta:
        model = models.Set
        fields = '__all__'

class CardsSetializer(serializers.ModelSerializer):

    class Meta:
        model = models.Card
        fields = '__all__'