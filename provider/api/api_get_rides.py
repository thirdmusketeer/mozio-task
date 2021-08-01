# Author: Third Musketeer
# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from shapely.geometry import Point, Polygon

from provider.models import ProviderServiceArea
from provider.api.serializers import ProviderServiceAreaSerializer


class RidesAPIView(APIView):
    """
        View to get all matching Rides

        * Requires lat/lng
    """
    def get(self, request):
        if 'lat' not in request.GET or 'lng' not in request.GET:
            return Response({"error": "lat, lng required"}, status=HTTP_400_BAD_REQUEST)
        try:
            lat = float(request.GET["lat"])
            lng = float(request.GET["lng"])
        except ValueError as e:
            return Response({"error": "lat, lng must be real numbers"}, status=HTTP_400_BAD_REQUEST)
        point = Point(lat, lng)
        rides = []
        # return Response(ProviderServiceArea.objects.first().polygon["coordinates"])
        for service_area in ProviderServiceArea.objects.all():
            polygon = Polygon(service_area.polygon["coordinates"])
            if point.within(polygon):
                rides.append(service_area)
        rides_data = ProviderServiceAreaSerializer(rides, many=True).data
        return Response(rides_data)