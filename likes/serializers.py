from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.ModelSerializer):
    """
    LikeSerializer to map the model instance into JSON format.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['owner', 'post', 'created_at']
        read_only_fields = ['created_at']
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })