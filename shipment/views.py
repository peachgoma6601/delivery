from django.shortcuts import render
from rest_framework import generics,status
import json
from rest_framework.response import Response
from shipment.serializers import ShipmentSeializer,TrackingSerializers
from rest_framework.views import APIView
import requests
from django.views.decorators.csrf import csrf_exempt

global data

@csrf_exempt
def inputs(request):
    return render(request,'addressForm.html')

class CreateShipment(APIView):
    def post(self,request):
        

        url = "https://api.easyship.com/v2/shipments"

        payload = {
            "origin_address": {
                "line_1": request.POST['senderAddress'],
                "state": request.POST['senderState'],
                "city": request.POST['senderCity'],
                "postal_code": request.POST['senderPostalCode'],
                "company_name": request.POST['senderCompanyName'],
                "contact_name": request.POST['senderContactName'],
                "contact_phone": request.POST['senderPhoneNumber'],
                "contact_email": request.POST['senderEmailAddress'],
            },
            "destination_address": {
                "line_1": request.POST['receiverAddress'],
                "city": request.POST['receiverCity'],
                "postal_code": request.POST['receiverPostalCode'],
                "country_alpha2": "IN",
                "contact_name": request.POST['receiverContactName'],
                "contact_email": request.POST['receiverEmailAddress'],
                "contact_phone": request.POST['receiverPhoneNumber'],
            },
            "incoterms": "DDU",
            "insurance": {"is_insured": False},
            "courier_selection": {
                "allow_courier_fallback": False,
                "apply_shipping_rules": True
            },
            "shipping_settings": {
                "units": {
                    "weight": "kg",
                    "dimensions": "cm"
                },
                "buy_label": False,
                "buy_label_synchronous": False,
                "printing_options": {
                    "format": "png",
                    "label": "4x6",
                    "commercial_invoice": "A4",
                    "packing_slip": "4x6"
                }
            },
            "parcels": [
                {
                    "total_actual_weight": 2,
                    "box": {
                        "length": request.POST['Length'],
                        "width": request.POST['Width'],
                        "height": request.POST['Height'],
                    },
                    "items": [
                        {
                            "quantity": 1,
                            "category": request.POST['Category'],
                            "description": request.POST['Description'],
                            "actual_weight": request.POST['actualWeight'],
                            "declared_currency": "INR",
                            "declared_customs_value": 500
                        }
                    ]
                }
            ]
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer prod_NxhNG5AjDR3CSWT9H9iNXi5FuzKFvN3Wlt/Pj/o53qA="
        }


        response = requests.post(url, json=payload, headers=headers)

        result = response.json()
        data = {
            'user':'test',
            'consignment' :result['shipment']['parcels'][0]['items'][0]['category'] ,
            'shipment_id' :result['shipment']['easyship_shipment_id'],
            'created_at' : result['shipment']['created_at'],
            'shipment_state': result['shipment']['shipment_state'],
            'tracking_url' :  result['shipment']['tracking_page_url']
        }

        serializer = ShipmentSeializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Tracking(APIView):
    def get(self,request):
        url = "https://api.easyship.com/track/v1/status?easyship_shipment_id=ESIN94700958"

        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer prod_NxhNG5AjDR3CSWT9H9iNXi5FuzKFvN3Wlt/Pj/o53qA="
        }

        response = requests.get(url, headers=headers)
        result = response.json()
        data = {
            'tracking_number':result['shipments'][0]['tracking_number'],
            'shipment_id':result['shipments'][0]['easyship_shipment_id'],
            'status':result['shipments'][0]['status'],
            'origin':result['shipments'][0]['origin'],
            'tracking_page_url':result['shipments'][0]['tracking_page_url'],
            'destination':result['shipments'][0]['destination'],
        }
        serializer = TrackingSerializers(data=data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
