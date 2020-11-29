from django.db import models
from rest_framework import serializers

from mainApp.models import QuoteCategory
from mainApp.models import Quote

class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory
        fields = ('__all__')

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote', 'author']