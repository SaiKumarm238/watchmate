from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from watchlist_app.api.serializers import ReviewSerializer,WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import StreamPlatform, WatchList, Review
# Create your tests here.


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="saikumar",password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamPlatform.objects.create(name= "Netflix",about ="No one stream platform",  website = "http://www.netflix.com" )
    
    def test_stream_platform_create(self):
        data = {
            "name": "Netflix",
            "about": "No one stream platform",
            "website":"http://www.netflix.com"            
        }
        
        response = self.client.post(reverse('stream'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_stream_platform_list(self):
        response = self.client.get(reverse('stream'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_stream_platform_ind(self):
        reapose = self.client.get(reverse('stream-detail', args=(self.stream.id,)))
        self.assertEqual(reapose.status_code, status.HTTP_200_OK)
        
    