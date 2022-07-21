from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorListSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorCreateListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def post(self, request):
        review = SensorListSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class MeasurementsCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class SensorsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})