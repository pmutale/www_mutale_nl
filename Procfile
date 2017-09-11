web: cd themes && npm install && cd themes && gulp production
web: gunicorn mysite.wsgi --log-file -
release: python manage.py migrate
release: python manage.py collectstatic -v0 --noinput
