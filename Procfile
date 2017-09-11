release: python manage.py migrate && cd themes && npm install && cd themes && gulp production && python manage.py collectstatic -v0 --noinput
web: gunicorn mysite.wsgi --log-file -
