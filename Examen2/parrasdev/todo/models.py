from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    userID = models.IntegerField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.title}"
