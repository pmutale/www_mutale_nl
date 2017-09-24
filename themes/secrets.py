def read_mailpass(user):
    import os

    try:
        mail = os.path.join(os.environ['HOME'], '.mail')
        mail_lines = open(mail).read().split()
    except IOError:
        pass
    else:
        for match in (user, '*'):
            for line in mail_lines:
                words = line.strip().split(':')
                if words[1] == match:
                    return {
                        'password': words[0],
                        'user': user,
                        'port': words[2],
                        'host': words[3],
                        'ssl': words[4],
                    }
    return {
        'host': 'smtp.strato.com',
        'user': '',
        'port': '',
        'ssl': '',
        'password': '*******'

    }


def get_cache():
  import os
  try:
    os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS'].replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
    os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
    return {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': { 'tcp_nodelay': True }
      }
    }
  except:
    return {
      'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
      }
    }