from django.contrib import admin
from testapp.models import TestModel
from testapp.tasks import api_test_task

class TestModelAdmin(admin.ModelAdmin):
    actions = ['test_celery']
    def test_celery(self, request, test_models):
        for test_model in test_models:
            api_test_task.delay(test_model.name)
    test_celery.short_description = "Enqueue celery test task (check app logs)"

admin.site.register(TestModel, TestModelAdmin)
