from django.db import models


class Event(models.Model):
    """
    A Liberation Philly event.
    """
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    address_title = models.CharField(max_length=255, blank=True)
    address_street = models.CharField(max_length=255)
    address_city = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_zip = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    level = models.ManyToManyField('Level', blank=True)
    contact = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True)
    ICON_CHOICES = (
        ('calendar', 'Calendar'),
        ('save', 'Save'),
        ('cube', 'Cube'),
        ('protest', 'Protest'),
        ('training', 'Training'),
        ('social', 'Social'),
    )
    icon = models.CharField(
        max_length=255,
        choices=ICON_CHOICES,
        default='calendar',
    )

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
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Email(models.Model):
    """
    A temporary way to collect emails from the sign up form until the email
    server gets fixed.
    """
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
