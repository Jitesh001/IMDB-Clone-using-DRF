from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser@123',
        )
        # Check if a token already exists for the user
        if not Token.objects.filter(user=self.user).exists():
            self.token = Token.objects.create(user=self.user)
        else:
            self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='Netflix',
            about='#1 NO.1 platfom',
            website= 'https://www.netflix.com')
        
    def test_streamplatfom_create(self):
        data= {
            'name': 'HBO',
            'about':'#1 NO.1 platfom',
            'website': 'https://www.hbo.com',
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=[self.stream.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class WatchListCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser@123',
        )
        # Check if a token already exists for the user
        if not Token.objects.filter(user=self.user).exists():
            self.token = Token.objects.create(user=self.user)
        else:
            self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='Netflix',
            about='#1 NO.1 platfom',
            website= 'https://www.netflix.com')
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title='Example movie1',
                                                         storyline='Awesome', active=True)
        
    def test_watlist_create(self):
        data = {
            'platform' : self.stream,
            'title' : 'Example movie',
            'storyline' : 'drama',
            'active': 'true'
        }
        response = self.client.post(reverse('watch-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_watchlist_ind(self):
        response = self.client.get(reverse('watch-detail', args=[self.watchlist.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, 'Example movie1') #checking if same movie created.
        
        
class ReviewListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testuser@123',
        )
        # Check if a token already exists for the user
        if not Token.objects.filter(user=self.user).exists():
            self.token = Token.objects.create(user=self.user)
        else:
            self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name='Netflix',
            about='#1 NO.1 platfom',
            website= 'https://www.netflix.com')
        
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title='Example movie1',
                                                         storyline='Awesome', active=True)
        
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title='Example movie2',
                                                         storyline='Awesome', active=True)
        self.review = models.Review.objects.create(review_user=self.user, rating=5, description='good movie'
                                                   , active=False, watchlist=self.watchlist2)
        
    def test_review_create(self):
            data = {
                'review_user':self.user,
                'rating':5,
                'description':'Good movie',
                'active': 'true',
                'watchlist': self.watchlist
                }
            
            response = self.client.post(reverse('review-create', args=[self.watchlist.id]), data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)   
            self.assertEqual(models.Review.objects.count(), 2)
            
    def test_review_create_unauth(self):
            data = {
                'review_user':self.user,
                'rating':5,
                'description':'Good movie',
                'active': 'true',
                'watchlist': self.watchlist
                }
            
            self.client.force_authenticate(user=None)
            response = self.client.post(reverse('review-create', args=[self.watchlist.id]), data)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 
            
    def test_review_update(self):
            data = {
                'rating':4,
                'description':'Average movie',
                'active': 'true'
                }
            
            response = self.client.put(reverse('review-detail', args=[self.review.id]), data)
            self.assertEqual(response.status_code, status.HTTP_200_OK) 
            
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=[self.watchlist.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                                   
    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=[self.review.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_user(self):
        response = self.client.get('/api/watchlist/user-reviews/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)