from rest_framework import generics

from mainApp.models import QuoteCategory
from mainApp.models import Quote

from .serializers import QuoteCategorySerializer
from .serializers import QuoteSerializer

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer
