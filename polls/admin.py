from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Add Question area into admin site
admin.site.register(Question)

# Add Choice area into admin site
admin.site.register(Choice)