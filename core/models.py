from django.db import models

class Event(models.Model):
    """
    A Liberation Philly event.
    """
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    link = models.URLField(max_length=255)
    tags = models.ManyToManyField('Tag')
    level = models.ManyToManyField('Level')
    contact = models.EmailField(max_length=255)


    def __str__(self):
        return self.title

class Level(models.Model):
    """
    The risk levels for a particular event.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Tag(models.Model):
    """
    The types of action present at a particular event.
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
