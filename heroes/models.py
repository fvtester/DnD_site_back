from django.db import models
from django.contrib.auth.models import User

class Heroes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="images/%Y/%m/%d")
    level = models.IntegerField()
    race = models.ForeignKey('Race', on_delete=models.PROTECT, null=True)
    hero_class = models.ForeignKey('HeroClass', on_delete=models.PROTECT, null=True)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class HeroClass(models.Model):
    class_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    bonuses = models.CharField(max_length=255, blank=True)

class Race(models.Model):
    race_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    bonuses = models.CharField(max_length=255, blank=True)
