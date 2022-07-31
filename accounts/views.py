# from rest_framework import generics
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth.models import User

# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from .serializers import UserSerializer, OperationsUserSerializer



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['customer_id'] = user.customer_id
#         return token


# class ObtainTokenPairWithColorView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

# class UserCreate(generics.CreateAPIView):
#     serializer_class = UserSerializer


# class OperationsUserCreate(generics.CreateAPIView):
#     serializer_class = OperationsUserSerializer


# from django.contrib.auth import authenticate
# class LoginView(APIView):
#     permission_classes = ()

#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_
#         ˓→BAD_REQUEST)


