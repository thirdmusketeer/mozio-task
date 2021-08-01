from rest_framework import viewsets

from provider.models import Provider, ProviderServiceArea
from provider.api.serializers import ProviderSerializer, ProviderServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ProviderServiceArea.objects.all()
    serializer_class = ProviderServiceAreaSerializer
