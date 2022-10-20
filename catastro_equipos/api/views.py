from rest_framework.response import Response 
from catastro_equipos.models import Product
from catastro_equipos.api.serializers import ProductSerializer
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class ProductListView(APIView):
    def get(self, request):
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            productos = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'El producto no se encuentra'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(productos)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            productos = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'El producto no se encuentra'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(productos, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
    def delete(self, request, pk):
        try:
            productos = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'El producto a eliminar no existe'}, status=status.HTTP_404_NOT_FOUND)
        productos.delete()
        return Response({'msg':'El producto ha sido eliminado exitosamente'}, status=status.HTTP_200_OK)            

# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':   
#         productos = Product.objects.all()
#         serializer = ProductSerializer(productos, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         de_serializer = ProductSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     if request.method == 'GET':
#         try:  
#             productos = Product.objects.get(pk=pk)
#             serializer = ProductSerializer(productos)
#             return Response(serializer.data)
#         except Product.DoesNotExist:
#             return Response({'Error': 'EL producto a consultar no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         productos = Product.objects.get(pk=pk)
#         de_serializer = ProductSerializer(productos, data.request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response({de_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         try:   
#             productos = Product.objects.get(pk=pk)
#             productos.delete()
#         except Product.DoesNotExist:
#             return Response({'Error': 'EL producto a consultar no existe'}, status=status.HTTP_404_NOT_FOUND)    
#         return Response({'msg': 'El producto fue eliminado exitosamente'}, status=status.HTTP_200_OK)    

