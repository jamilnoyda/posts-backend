from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import Group
from rest_framework import viewsets
from accounts.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core import serializers

import json
from accounts.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def profile(self, request, pk=None):
        # request.user
        # import pdb; pdb.set_trace()
        # data = serializers.serialize('json',request.user[0] )
        
        return Response(UserSerializer(instance=request.user).data)

        # return Response(vars())

 


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]









