from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.tasks import send_welcome_email_task
from rest_framework.decorators import action
# Create your views here.

class RegisterViewset(viewsets.ModelViewSet):
    queryset=User.objects.filter()
    serializer_class=RegisterSerializer
    permission_classes=[IsAuthenticated]


    def get_permissions(self):
        if self.action == "create":
            self.permission_classes =[AllowAny]
        return super().get_permissions()
    
    # def get_serializer_class(self):
    #     if self.method == "POST":
    #         return RegisterSerializer

    def get_queryset(self):
        return User.objects.filter(is_staff=False)


    # def list(self,request):
    #     queryset=self.queryset.exclude(is_staff=True)
    #     serializer=self.serializer_class(queryset,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    
    
    @action(["get"], detail=False, url_path="profile")
    def me(self, request, *args, **kwargs):
        data = cache.get_or_set(f'user_{request.user.id}',request.user)
        if data is None:
            print()
            print("inside")
            print()
            cache.set(f'user_{request.user.id}',request.user)
            # cache.clear()
        print()
        print(data)
        print()
        instance=data
        serializer=self.serializer_class(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_welcome_email_task.delay(user.first_name,user.last_name,user.email)  # Optional: Use Celery here
        return Response({'message': 'User created and email sent!'}, status=status.HTTP_201_CREATED)
