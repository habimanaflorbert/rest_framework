from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.tasks import send_welcome_email_task
# Create your views here.

class RegisterViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_welcome_email_task.delay(user.first_name,user.last_name,user.email)  # Optional: Use Celery here
        return Response({'message': 'User created and email sent!'}, status=status.HTTP_201_CREATED)
