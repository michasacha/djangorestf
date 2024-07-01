from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from .models import Product 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializer import productSerializer

@api_view()
def api_view(request):
    #request different de requests
    # if request.method != "POST":
    #     return Response({'detail': 'method not allowed'}, status=405)
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
    #    data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount' ))
         data = productSerializer(query).data
    #serialization: mettre des donnees sur forme de dictionnaire 
    return Response(data)
# Create your views here.
