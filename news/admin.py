from django.contrib import admin
from .models import Company, News

# Register your models here.
admin.site.register([Company, News])
