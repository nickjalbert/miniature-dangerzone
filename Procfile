web: gunicorn miniature_dangerzone.wsgi -b 0.0.0.0:$PORT -w 9 --max-requests 250
celeryd: python manage.py celeryd -E -B --loglevel=INFO
