from home.models import (Student,School)
from home.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny,BasePermission
# Create your views here.

class StudentViews(APIView):

    def get(self,request):
        q=Student.objects.all()
        serializer=StudentSerializer(q,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SchoolViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[AllowAny]

    def list(self,request):
        print("dadaasdadas")
        return super().list(self.request)
    
    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


