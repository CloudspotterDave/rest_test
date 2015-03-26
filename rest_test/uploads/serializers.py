from django.contrib.auth.models import User
from rest_framework import serializers
from uploads.models import Upload

class UploadSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Upload
        fields = ('id', 'pic_url', 'created', 'owner')

class UserSerializer(serializers.ModelSerializer):
    uploads = serializers.PrimaryKeyRelatedField(many=True, queryset=Upload.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'uploads')
