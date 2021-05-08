from rest_framework import serializers
from .models import Advisor


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Advisor
        fields = ['id', 'advisor_name', 'photo_url', 'poster', 'created', 'poster_id']
