import mongoengine


class Task(mongoengine.Document):
    title = mongoengine.StringField(max_length=50, required=True)
    description = mongoengine.StringField(max_length=255)
    done = mongoengine.BooleanField(default=False)
