from rest_framework import generics
from firouzeh_digital.urls.models import URL
from .serializers import ShortenedURLSerializer

class CreateShortURL(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = ShortenedURLSerializer

class RedirectShortURL(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = ShortenedURLSerializer
    lookup_field = 'short_url'
