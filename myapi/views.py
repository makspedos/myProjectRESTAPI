import requests
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

class DataResponse(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is None:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            products = self.get_object(pk)
            serializer = ProductSerializer(products)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(f'Deleted object with id={pk}')

@api_view(['GET'])
def simpleParse(request):
    url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
    response = requests.get(url)
    data = response.json()
    print(data)
    return Response(data)