from rest_framework import serializers
from .models import Profile,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('Bio', 'photo', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'projectscreenshot','projecturl','user')        