from rest_framework_mongoengine import routers, serializers, viewsets

from DjangoMongo.core.models import Task


class TaskSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "done"]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


router = routers.DefaultRouter()
router.register("tasks", TaskViewSet)
