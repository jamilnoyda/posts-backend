from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["url", "email", "groups"]
        fields = "__all__"



class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = "__all__"

        # fields = ["url", "name"]

