from rest_framework import serializers
from meme.models import *


# Creating Serializer Class of ContentImage(Model)
class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'
