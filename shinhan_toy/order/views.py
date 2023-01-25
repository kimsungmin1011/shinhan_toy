from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status, mixins, generics
from .models import Order
from .serializers import OrderSerializer

class Orderview(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=OrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)