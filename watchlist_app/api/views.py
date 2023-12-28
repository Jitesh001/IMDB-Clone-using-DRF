from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django.shortcuts import get_object_or_404
from django.http import Http404 
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from watchlist_app.api.throttling import ReviewCreateThrottle, ReviewListThrottle #custom throttling
from watchlist_app.api.serializers import  WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamPlatform, Review

class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        queryset = Review.objects.filter(review_user__username=username)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return self.no_reviews_response()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def no_reviews_response(self):
        return Response({"message": "No reviews found for the specified use"})

    
class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewCreateThrottle]
    queryset = Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('watch_id')
        try:
            item = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise ValidationError('WatchList item not found')
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=item, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError('Thanks!, lready reviewed by you!')
    
        serializer.save(watchlist=item, review_user = review_user)
    
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer 
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']        #fields to filter
    
    #filter reviews having the same movie id provided in url
    def get_queryset(self):
        pk = self.kwargs['watch_id']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    # throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response({"message": "No review found"}, status=status.HTTP_404_NOT_FOUND)
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #         return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    #     except Http404:
    #         return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
 
#has all methods of viewsets (list, retrieve, create, delete etc.)   
class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            return Response({'msg': 'Stream platform deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist:
            return Response({'msg': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND)
    
class WatchListAV(APIView):
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request):
        content = WatchList.objects.all()
        serializer = WatchListSerializer(content, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class WatchListDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request, watch_id):
        try:
            content = WatchList.objects.get(pk=watch_id)
        except WatchList.DoesNotExist:
            return Response({'msg':'content not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(content)
        return Response(serializer.data)
    
    def put(self, request, watch_id):
        content = WatchList.objects.get(pk=watch_id)
        serializer = WatchListSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)    
    
    def delete(self, request, watch_id):
        try:
            content = WatchList.objects.get(pk=watch_id)
            content.delete()
            return Response({'msg': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({'msg': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)