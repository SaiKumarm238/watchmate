from urllib import response
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
        
        """
        To setUp any data to test we have written hear in the  def setUp 
        """
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
        
class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="saikumar",password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamPlatform.objects.create(name= "Netflix",about ="No one stream platform",  website = "http://www.netflix.com" )
        
        self.watchlist = WatchList.objects.create(title = "Test Movie",storyline="Test Movie Storyline",platform= self.stream,active= True)
        
        
    def test_watchlist_create(self):
        
        data = {
            "platform": self.stream,
            "title": "Test Movie",
            "storyline": "Test Movie Storyline",
            "active" : True
        }
        
        response = self.client.post(reverse('movie-list'), data=data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        
    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(WatchList.objects.count(),1)
        self.assertEqual(WatchList.objects.get().title, "Test Movie")
            
class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="saikumar",password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = StreamPlatform.objects.create(name= "Netflix",about ="No one stream platform",  website = "http://www.netflix.com" )
        
        self.watchlist = WatchList.objects.create(title = "Test Movie",storyline="Test Movie Storyline",platform= self.stream,active= True)
        
        self.watchlist2 = WatchList.objects.create(title = "Test Movie2",storyline="Test Movie Storyline2",platform= self.stream,active= True)
        
        self.review = Review.objects.create(review_user = self.user, rating=5,description="Good Movie",  watchlist = self.watchlist2, active=True)
        
    def test_review_create(self):
        data = {
            "review_user":self.user,
            "rating":5,
            "description":"Good Movie",
            "watchlist":self.watchlist,
            "active":True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Review.objects.count(),2)
        #self.assertEqual(Review.objects.get().rating, 5)
       
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_review_create_unauth(self):
        data = {
            "review_user":self.user,
            "rating":5,
            "description":"Good Movie",
            "watchlist":self.watchlist,
            "active":True
        }
        
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update_(self):
        data = {
            "review_user":self.user,
            "rating":4,
            "description":"Good Movie ok ok - update ",
            "watchlist":self.watchlist,
            "active":False
        }
        
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)