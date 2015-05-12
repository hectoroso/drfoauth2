from django.contrib.auth.models import User, Group

from rest_framework import viewsets, routers
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] # TokenHasReadWriteScope
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
