web: gunicorn mysite.wsgi --log-file -
worker: npm install
release: python manage.py collectstatic -v0 --noinput
release: python manage.py migrate