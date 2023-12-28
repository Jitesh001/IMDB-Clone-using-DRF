from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist',null=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=400, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self):
        return str(self.rating) + '|' + self.watchlist.title + '|' + str(self.review_user)
    
    def save(self, *args, **kwargs):
        # Call the parent class's save method to save the review
        super().save(*args, **kwargs)

        # Update WatchList averages and number of ratings
        item = self.watchlist
        reviews = Review.objects.filter(watchlist=item)
        num_ratings = reviews.count()
        avg_rating = sum(review.rating for review in reviews) / num_ratings if num_ratings > 0 else 0

        item.number_rating = num_ratings
        item.avg_rating = avg_rating
        item.save()
        
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.update_watchlist()

    def update_watchlist(self):
        # Update WatchList averages and number of ratings
        item = self.watchlist
        reviews = Review.objects.filter(watchlist=item, active=True)
        num_ratings = reviews.count()
        avg_rating = sum(review.rating for review in reviews) / num_ratings if num_ratings > 0 else 0

        item.number_rating = num_ratings
        item.avg_rating = avg_rating
        item.save()
        
@receiver(post_delete, sender=Review)
def update_watchlist_on_review_delete(sender, instance, **kwargs):
    instance.update_watchlist()