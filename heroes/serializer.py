from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Heroes


class UserSerializer(serializers.ModelSerializer):
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
