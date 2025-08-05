# accounts/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(required=True,write_only=True)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    email=serializers.EmailField(required=True)

    def validate(self, attrs):
        if attrs.get('password')!= attrs.get('re_password'):
            raise  serializers.ValidationError("Password not match")
        return super().validate(attrs)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password','re_password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user
