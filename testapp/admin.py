from django.contrib import admin
from testapp.models import TestModel

class TestModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(TestModel, TestModelAdmin)
