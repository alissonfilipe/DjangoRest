# serializers = gera JSON dos modelos

from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Usertasks
        # fields = ['user_nickname', 'user_task']'