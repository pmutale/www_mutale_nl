web: cd themes && npm install && cd themes && gulp production
web: gunicorn mysite.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic -v0 --noinput
