release: python manage.py migrate
release: cd themes && npm install
release: cd themes && gulp production
release: python manage.py collectstatic -v0 --noinput
web: gunicorn mysite.wsgi --log-file -
