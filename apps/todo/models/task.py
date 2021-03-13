from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse, NoReverseMatch
from django.utils import timezone

from apps.todo.manager import DueTaskManager, FullEmptyCategory


# category of a task
class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100, verbose_name='name', unique=True)  # Like a varchar
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name  # name to be shown when called

    objects = FullEmptyCategory()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# class of task
class Task(models.Model):  # Task list able name that inherits models.Model
    title = models.CharField('Title', max_length=250, unique=True)  # a varchar
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    description = models.TextField('Description', blank=True)  # a text field
    PRIORITY_CHOICE = [('High', 'high'), ('Middle', 'middle'), ('Low', 'low')]
    priority = models.CharField('Priority', max_length=6, blank=True, choices=PRIORITY_CHOICE)
    due_date = models.DateTimeField('Due Date And Time', default=timezone.now())  # a date
    category = models.ForeignKey('Category', default="general", on_delete=models.PROTECT)  # a foreignkey
    done = models.BooleanField('Done', default=False)

    class Meta:
        ordering = ["-due_date"]  # ordering by the due_date field

    def __str__(self):
        return self.title  # name to be shown when called

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        try:
            return reverse('taskdetail', args=[str(self.id)])
        except NoReverseMatch:
            return reverse('404')

    objects = DueTaskManager()
