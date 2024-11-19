from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from django.contrib.auth.models import User
from django.db import models, transaction
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    # User fields
    password = serializers.CharField(source='user.password', write_only=True, required=True)
    email = serializers.CharField(source='user.email', required=True)

    # UserProfile fields
    doc_type = serializers.CharField(max_length=6)
    doc_num = serializers.IntegerField()
    first_name = serializers.CharField(max_length=30)
    second_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=60)
    birth_date = serializers.DateField()
    gender = serializers.CharField(max_length=50)
    cel_num = serializers.CharField(max_length=20)
    image = serializers.ImageField()
    
    class Meta:
        model = UserProfile
        fields = ['password', 'email', 'doc_type', 'doc_num', 'first_name', 'second_name', 
                  'last_name', 'name_origin', 'birth_date', 'gender', 'cel_num', 'image']

    def create(self, validated_data):
        try:
            with transaction.atomic():        
                user_data = {
                    'username': validated_data['user']['email'],
                    'password': validated_data['user']['password'],
                    'email': validated_data['user']['email']
                }
                user = User.objects.create_user(**user_data)
                
                name_origin = self.get_origin_from_gemini(validated_data['first_name'])
                user_profile_data = {key: validated_data[key] for key in ['doc_type', 'doc_num', 'first_name', 
                                                                        'second_name', 'last_name', 'birth_date', 
                                                                        'gender', 'cel_num', 'image']}
                user_profile_data['name_origin'] = name_origin
                user_profile = UserProfile.objects.create(user=user, **user_profile_data)
                
                return user_profile
        except Exception as e:
            user.delete()
            raise e
    
    def get_origin_from_gemini(self, name):
        return "Hebrew"
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token