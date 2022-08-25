# customers/backends.py
from asyncio import exceptions
from logging import raiseExceptions
from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import exceptions

class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, type=None, **kwargs):
        print('gets here in BACKEND!!!!!!')
        # print(request.POST)        
        # username = request.POST['username']
        # # type = request.POST['type']
        # password = request.POST['password']
        user = get_user_model().objects.filter(username=username).first()
        # try:
        #     user = User.objects.get(username=username)
        #     if user.check_password(password) is True:
        #         if user.type == type:
        #             return user
        # except User.DoesNotExist:
        #     pass        
        if user is None:
            raise exceptions.AuthenticationFailed("User not Found!")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect is Password")
        # if not user.type == type:
        #     raise exceptions.AuthenticationFailed("Incorrect Password or Username")
        print(user)
        return user
    # def access_token(self):               
    #     return get_tokens_for_user()




	