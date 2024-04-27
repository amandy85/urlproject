from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # host(r'blog', 'urlproject.hostsconf.urls', name='blog'),
    host(r'(?!www).*', 'urlproject.hostsconf.urls', name='wildcard'),
)