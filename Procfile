release: python manage.py migrate
release: python manage.py collectstatic -v0 --noinput
web: gunicorn mysite.wsgi --log-file -
web: bin/web
worker: bin/worker
