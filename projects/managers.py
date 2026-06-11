from django.db import models


class ProjectQuerySet(models.QuerySet):

    def active(self):
        return self.filter(status="active")

    def completed(self):
        return self.filter(status="completed")

    def high_budget(self):
        return self.filter(budget__gte=500000)


class ProjectManager(models.Manager):

    def get_queryset(self):
        return ProjectQuerySet(self.model,using=self._db)

    def active(self):
        return self.get_queryset().active()

    def high_budget(self):
        return self.get_queryset().high_budget()