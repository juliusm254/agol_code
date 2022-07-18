# customers/backends.py
from asyncio import exceptions
from logging import raiseExceptions
from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import exceptions

class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, type=None, **kwargs):
        print('gets here')
        print(request)        
        username = request['username']
        type = request['type']
        password = request['password']
        User = get_user_model().objects.filter(username=username).first()
        # try:
        #     user = User.objects.get(username=username)
        #     if user.check_password(password) is True:
        #         if user.type == type:
        #             return user
        # except User.DoesNotExist:
        #     pass        
        if User is None:
            raise exceptions.AuthenticationFailed("User not Found!")
        if not User.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect is Password")
        if not User.type == type:
            raise exceptions.AuthenticationFailed("Incorrect Password or Username")
        
        return User
    # def access_token(self):               
    #     return get_tokens_for_user()




	