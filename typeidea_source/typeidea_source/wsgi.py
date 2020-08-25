"""
WSGI config for typeidea_source project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea_source.settings.%s' % profile)

application = get_wsgi_application()
