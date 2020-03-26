from rest_framework_mongoengine import serializers

from DjangoMongo.core.models import Task


class TaskSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "done"]
