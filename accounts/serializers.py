from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# ...
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'customer_id', 'type', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        User = get_user_model()
        user = User(
        customer_id=validated_data['customer_id'],
        username=validated_data['username'],
        type=validated_data['type']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
