from django.db import models


class TaskQuerySet(models.QuerySet):

    def pending(self):
        return self.filter(status="pending")

    def completed(self):
        return self.filter(status="completed")

    def high_priority(self):
        return self.filter(priority="high")


class TaskManager(models.Manager):

    def get_queryset(self):
        return TaskQuerySet(self.model,using=self._db)

    def pending(self):
        return self.get_queryset().pending()

    def high_priority(self):
        return self.get_queryset().high_priority()