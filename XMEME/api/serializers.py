from rest_framework import serializers
from meme.models import *

class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'
