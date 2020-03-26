from rest_framework_mongoengine import viewsets

from DjangoMongo.core.models import Task
from DjangoMongo.core.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
