from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
    return render_to_response(
            'testapp/index.html',
            {},
            context_instance=RequestContext(request))

