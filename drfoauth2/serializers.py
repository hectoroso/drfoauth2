from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

# from http://www.yeti.co/blog/oauth2-with-django-rest-framework/
class SignUpSerializer(serializers.ModelSerializer):
    client_id = serializers.SerializerMethodField('get_client_id')
    client_secret = serializers.SerializerMethodField('get_client_secret')

    class Meta:
        model = User
        fields = ('username', 'password', 'client_id') #, 'client_secret'
        write_only_fields = ('password',)

    def get_client_id(self, obj):
        try:
            return obj.oauth2_provider_application.first().client_id
        except AttributeError:
            return None

    def get_client_secret(self, obj):
        try:
            return obj.oauth2_provider_application.first().client_secret
        except AttributeError:
            return None

class LoginSerializer(serializers.ModelSerializer):
    client_id = serializers.SerializerMethodField('get_client_id')
    class Meta:
        model = User
        fields = ('username', 'password', 'client_id')
        write_only_fields = ('password',)

    def get_client_id(self, obj):
        try:
            return obj.oauth2_provider_application.first().client_id
        except AttributeError:
            return None
