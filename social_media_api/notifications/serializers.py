# notifications/serializers.py
from rest_framework import serializers
from django.conf import settings
from .models import Notification

UserModel = settings.AUTH_USER_MODEL


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


class NotificationSerializer(serializers.ModelSerializer):
    actor = SimpleUserSerializer(read_only=True)
    recipient = SimpleUserSerializer(read_only=True)
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id',
            'recipient',
            'actor',
            'verb',
            'target',
            'timestamp',
            'is_read',
        )
        read_only_fields = (
            'id',
            'recipient',
            'actor',
            'verb',
            'target',
            'timestamp',
        )

    def get_target(self, obj):
        target = getattr(obj, 'target', None)
        if target is None:
            return None

        # attempt to get an id attribute and a readable representation
        target_id = getattr(target, 'id', None)
        try:
            target_repr = str(target)
        except Exception:
            target_repr = None

        return {
            'type': obj.target_content_type.model if obj.target_content_type else None,
            'id': target_id,
            'repr': target_repr,
        }


class NotificationMarkReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'is_read')
        read_only_fields = ('id',)
