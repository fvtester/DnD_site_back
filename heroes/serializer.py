from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Heroes


class UserSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    picture = serializers.ImageField()
    level = serializers.IntegerField()
    race = serializers.IntegerField()
    hero_class = serializers.IntegerField()
    strength = serializers.IntegerField(default=0)
    dexterity = serializers.IntegerField(default=0)
    constitution = serializers.IntegerField(default=0)
    intelligence = serializers.IntegerField(default=0)
    wisdom = serializers.IntegerField(default=0)
    charisma = serializers.IntegerField(default=0)
    hit_points = serializers.IntegerField(default=0)
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class HeroesSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Heroes
        fields = ('id', 'user', 'name', 'description', 'picture',
                  'level', 'race', 'hero_class', 'strength', 'dexterity', 'constitution',
                  'intelligence', 'wisdom', 'charisma', 'hit_points')
