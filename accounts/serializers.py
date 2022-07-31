# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from .models import CustomerUser, OperationsUser
# from rest_framework.authtoken.models import Token

# # ...
# class UserSerializer(serializers.ModelSerializer): 
#     class Meta:
#         User = get_user_model()
#         model = User
#         fields = ('username', 'customer_id', 'type', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

    
#     def create(self, validated_data):
#         User = get_user_model()
#         user = User(
#         customer_id=validated_data['customer_id'],
#         username=validated_data['username'],
#         type=validated_data['type']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user

# class OperationsUserSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = OperationsUser
#         fields = ('username', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

    
#     def create(self, validated_data):
#         user = OperationsUser(
#         username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user
