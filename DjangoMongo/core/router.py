from rest_framework_mongoengine import routers

from DjangoMongo.core.views import TaskViewSet

router = routers.SimpleRouter()
router.register("tasks", TaskViewSet)
