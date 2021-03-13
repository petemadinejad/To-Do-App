from django.db import models
from django.db.models.functions import Now


# this manager is for task
class DueTaskManager(models.Manager):
    def get_passed_tasks(self):
        data = super().get_queryset().filter(due_date__lt=Now())
        return data


# this manager is for category
class FullEmptyCategory(models.Manager):
    def get_empty_category(self):
        return self.filter(task=None)

    def get_full_category(self):
        return self.exclude(task=None)
