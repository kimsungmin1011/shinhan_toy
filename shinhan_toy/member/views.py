from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, mixins, generics
from .models import Member
from .serializers import MemberSerializer

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,*args,**kwargs):
        # 로그인한 사용자만 들어올 수 있는 곳
        username=request.data.get('username')
        current = request.data.get('current')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if password1 != password2:
            return Response ({
                'detail' : 'Wrong new passwords',
            }, status=status.HTTP_400_BAD_REQUEST)
            
        member = request.user
        if not check_password(current, member.password):
            return Response({
                'detail' : 'Wrong password'
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password1)
        member.save()

        return Response(status=status.HTTP_200_OK)


# Create your views here.
