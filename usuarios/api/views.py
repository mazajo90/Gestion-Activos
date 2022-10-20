from rest_framework.response import Response
from usuarios.models import User
from usuarios.api.serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView

class UserListView(APIView):
    def get(self, request):
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            ususarios = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'El usuario no se encuentra'}, status=status.HTTP_404_NOT_FONUD)
        serializer = UserSerializer(usuarios)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            usuarios = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'El usuario no se encuentra'}, status=status.HTTP_404_NOT_FONUD)
        serializer = UserSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            usuarios = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'El usuario a eliminar no existe'}, status=status.HTTP_404_NOT_FONUD)
        usuarios.delete()
        return Response({'msg': 'Usuario eliminado exitosamente'}, status=status.HTTP_200_OK)                    