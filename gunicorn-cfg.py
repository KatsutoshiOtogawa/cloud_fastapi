"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

PORT = os.environ.get('PORT')
BIND = os.environ.get('BIND')
workers = os.environ.get('WORKERS')


bind = BIND + ':' + PORT
# accesslog = os.environ.get('ACCESSLOG')

# loglevel = os.environ.get('LOGLEVEL')
# capture_output = os.environ.get('CAPTURE_OUTPUT')
# enable_stdio_inheritance = os.environ.get('ENABLE_STDIO_INHERITANCE')
