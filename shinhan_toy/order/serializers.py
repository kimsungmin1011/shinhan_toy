from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8: # 비밀번호가 짧을시
            raise serializers.ValidationError('Too short password')
        # 유효성 검사가 끝난 값을 반환
        return make_password(value)

    class Meta:
        model = Order
        fields='__all__'