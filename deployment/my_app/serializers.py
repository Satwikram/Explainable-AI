from .models import *
from rest_framework import serializers


class PredictSerializer(serializers.ModelSerializer):

    class Meta:
        model = SceneImage
        fields = [
            'id',
            'image_path',
            'prediction'
        ]
