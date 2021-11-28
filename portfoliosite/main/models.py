from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='portfolios',
                               blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.id}]Portfolio: {self.name}"

    def get_absolute_url(self):
        return "/portfolio/" + str(self.id)


class Image(models.Model):
    portfolio = models.ForeignKey(Portfolio,
                                  on_delete=models.CASCADE,
                                  related_name='images',
                                  blank=False)
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(verbose_name='/images/', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.id}]Image: '{self.name}'"

    def get_absolute_url(self):
        return "/image/" + str(self.id)


class Comment(models.Model):
    image = models.ForeignKey(Image,
                              on_delete=models.CASCADE,
                              related_name='comments',
                              blank=False)
    name = models.CharField(max_length=64, blank=False)
    body = models.TextField(blank=False)

    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)  # for manual deactivation by the administrator

    def __str__(self):
        return "[{self.id}]Comment: from {self.name} on [{self.image.id}]{self.image}"
