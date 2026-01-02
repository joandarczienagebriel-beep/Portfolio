from django.conf import settings
from django.db import models
from django.urls import reverse
#africa
class BookReview(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body=models.TextField()
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-date']

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk':self.pk})
    
class Comment(models.Model):
    bookreview=models.ForeignKey(BookReview, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.comment
#west-europe

class Europe(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body=models.TextField()
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date']

    def get_absolute_url(self):
        return reverse("europe_detail", kwargs={"pk": self.pk})
    
class CommentEurope(models.Model):
    europe=models.ForeignKey(Europe, on_delete=models.CASCADE, default= 'Blank')
    comment=models.CharField(max_length=200)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.comment

class Message(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=100)
    Message=models.TextField()
