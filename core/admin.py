from django.contrib import admin
from .models import Event, Level, Tag, Email

admin.site.register(Event)
admin.site.register(Level)
admin.site.register(Tag)
admin.site.register(Email)
