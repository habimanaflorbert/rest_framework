from home.models import (Student,School)
from home.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from home.permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from home.serializers import MyTokenObtainPairSerializer
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
    permission_classes=[IsAuthenticated]

    def list(self,request):
        print("dadaasdadas")
        return super().list(self.request)
    
    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class MyAuthenticationView(APIView):
    # authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    # def get_permissions(self):
    #     if self.request.method=="GET":
    #         return [IsOwnerOrReadOnly()]
    #     return super().get_permissions()

    def get(self,request):
        print()
        print(request.__dict__)
        print()
        return Response({'username':"Welcome"},status=status.HTTP_200_OK)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        print()
        print(response)
        print()
        try:
            token = Token.objects.get(key=response.data['token'])
        except Token.DoesNotExist:
            return Response({"msg":"something wrong !"},status=status.HTTP_401_UNAUTHORIZED) 
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
        })
    


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer