from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from testapp.models import TestModel

def home(request):
    return render_to_response(
            'testapp/index.html',
            {'test_apps': TestModel.objects.all()},
            context_instance=RequestContext(request))

