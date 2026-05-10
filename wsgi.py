import os
from django.core.wsgi import get_wsgi_application

# Asegúrate de que aquí diga 'settings' (sin tildes)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
