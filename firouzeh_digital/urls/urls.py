from django.urls import path
from .api import views

urlpatterns = [
    path('shorten/', views.CreateShortURL.as_view(), name='shorten-url'),
    path('<str:short_url>/', views.RedirectShortURL.as_view(), name='redirect-url'),
]
