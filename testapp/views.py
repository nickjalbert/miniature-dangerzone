from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from testapp.models import TestModel
from testapp.forms import TestModelForm

def home(request):
    errors = ''
    if request.method == 'POST':
        form = TestModelForm(request.POST, request.FILES)
        if not request.user.is_staff:
            errors += "Only Staff can create new entries. "
        elif form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('testapp.views.home'))
    else:
        form = TestModelForm()
    return render_to_response(
            'testapp/index.html',
            {
                'test_apps': TestModel.objects.all(),
                'form': form,
                'errors': errors,
            },
            context_instance=RequestContext(request))

