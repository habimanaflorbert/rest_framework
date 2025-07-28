from rest_framework import serializers
from home.models import (School,Student)

class StudentSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=Student
        fields=['id','first_name','last_name','email','date_ofBirth','subject','gender','image']
    
    def validate_email(self,email):
        if Student.objects.filter(email=email).exists():
            print("fdfsfsfsdfsf")
            raise  serializers.ValidationError("Email is exists")
        return email
        

    def create(self, validated_data):
        return Student.objects.create(first_name=validated_data.get("first_name"),last_name=validated_data.get('last_name'),
                                      email=validated_data['email'],date_ofBirth=validated_data['date_ofBirth'],
                                      subject=validated_data['subject'],gender=validated_data['gender'],image=validated_data['image'])
    
class SChoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','first_name','last_name','email','date_ofBirth','subject','gender','image']
