from django.contrib import admin

# Register your models here.
from .models import Candidate
from .models import TestScore


admin.site.register(Candidate)
admin.site.register(TestScore)
