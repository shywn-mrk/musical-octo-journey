from rest_framework import serializers
from firouzeh_digital.urls.models import URL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'long_url', 'short_url']
        read_only_fields = ['short_url']
