from django.urls import path

from django.contrib import admin
from .views import SensorCreateListView, SensorsRetrieveUpdateAPIView, MeasurementsCreateAPIView


urlpatterns = [
    path('sensors/', SensorCreateListView.as_view()),
    path('sensors/<pk>/', SensorsRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementsCreateAPIView.as_view())

]