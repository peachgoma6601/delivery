from  django.urls import path
from . import views

urlpatterns = [
    path('shipment/',views.CreateShipment.as_view(),name='shipment'),
    path('tracking/',views.Tracking.as_view()),
    path('test/',views.inputs,name='test')
]