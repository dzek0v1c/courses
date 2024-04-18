from django.db import models
from .CustomUser import CustomUser
from .Lesson import Lesson

class Course(models.Model) :
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey (CustomUser, on_delete = models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

    def __str__(self):
        return self.name