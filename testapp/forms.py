from django.forms import ModelForm
from testapp.models import TestModel

class TestModelForm(ModelForm):
    class Meta:
        model = TestModel

