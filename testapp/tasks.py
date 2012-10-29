from celery import Celery
from django.conf import settings
from captools.api import Client

celery = Celery('testapp', broker='django://guest@localhost//')

@celery.task
def api_test_task(name):
    client = Client(settings.CAPTRICITY_API_TOKEN)
    jobs = client.read_jobs()
    print 'Enqueued object name: %s' % name
    print 'Your jobs are:'
    for job in jobs:
        print '\t%s' % job.get('name')
