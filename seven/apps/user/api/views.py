# from django.contrib.auth.models import User
# rest_framework
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView, ListAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# Models
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User, Token

from .serializers import UserCreateSerializer, UserUpdateSerializer, ChangePasswordSerializer
from config.authentication import MyTokenAuthentication


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    def perform_create(self, serializer):
        # Hash User Password
        posted_data = serializer.validated_data
        hashed_password = make_password(posted_data['password'])
        posted_data['password'] = hashed_password
        return serializer.save()


class UserLoginView(APIView):

    def post(self, *args, **kwargs):
        posted_data = self.request.data

        try:
            username = posted_data['username']
        except MultiValueDictKeyError:
            return Response({
                "Error": "Empty username"
            })

        try:
            password = posted_data['password']
        except MultiValueDictKeyError:
            return Response({
                "Error": "Empty password"
            })

        try:
            user = User.objects.get(username = username)
        except ObjectDoesNotExist:
            return Response({
                "Error": "This user not found"
            })

        if check_password(password=password, encoded=user.password):
            # make the user active and authenticated True
            user.is_active = True
            user.is_authenticated = True
            user.save()
            # get a serialized json of the user
            user_json = UserCreateSerializer(user)
            try:
                token =  Token.objects.get(user=user)
                return Response({
                    "token": token.key,
                    "user": user_json.data
                })
            except ObjectDoesNotExist:
                return Response({
                    "token": "",
                    "user": user_json.data
                })

        return Response({
            "Error": "incorrect password"
        })


class UserRUD(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = User.objects.filter(is_active=True).order_by('-id')
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (MyTokenAuthentication,)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (MyTokenAuthentication,)


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (MyTokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            old_password = request.data['old_password']
        except MultiValueDictKeyError:
            return Response({"Error": "old_password not valid"})
        try:
            new_password = request.data['new_password']
        except MultiValueDictKeyError:
            return Response({"Error": "new_password not valid"})
        try:
            re_new_password = request.data['re_new_password']
        except MultiValueDictKeyError:
            return Response({"Error": "re_new_password not valid"})

        try:
            user = User.objects.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            return Response({"Error": "user not found"})
        if check_password(password=old_password, encoded=user.password):
            if new_password == re_new_password:
                hashed_password = make_password(new_password)
                user.password = hashed_password
                user.save()
                return Response({"Success": "password changed"}, status=200)
            else:
                return Response({"Error": "new and renew password not matched"}, status=404)
        else:
            return Response({"Error": "Incorrect Old Password"})