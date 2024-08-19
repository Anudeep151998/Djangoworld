"""
WSGI config for Newwor1d project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application

try:
    # Set the default settings module for the 'django' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Newwor1d.settings')

    # Get the WSGI application for the Django project.
    application = get_wsgi_application()

except Exception as e:
    # Print the error message and stack trace to stderr
    print(f"Error: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)

    # Optionally, you could also log errors to a file or external service
    # with open('/path/to/error.log', 'a') as log_file:
    #     log_file.write(f"Error: {e}\n")
    #     traceback.print_exc(file=log_file)
    
    # Re-raise the exception to ensure that WSGI server handles it appropriately
    raise
