web: gunicorn mysite.wsgi --log-file -
release: python manage.py collectstatic -v0 --noinput
release: python manage.py migrate
worker:  npm --prefix ./themes/ install