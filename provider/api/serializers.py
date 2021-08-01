# Author: Third Musketeer
# -*- coding: utf-8 -*-
from rest_framework import serializers
from provider.models import Provider, ProviderServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "email", "phone_number", "language", "currency")


class ProviderMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "currency")


class ProviderServiceAreaSerializer(serializers.ModelSerializer):
    provider = ProviderMiniSerializer(read_only=True)

    class Meta:
        model = ProviderServiceArea
        fields = ("name", "provider", "price", "polygon")
