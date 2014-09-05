#!/usr/bin/env python

import os
import sys

import nose


# Set up the environment for our test project.
ROOT = os.path.abspath(os.path.dirname(__file__))

# import to check for the existence of Django
import django
DJANGO_SETTINGS_MODULE="django_spicedham.settings"
os.environ.update({'DJANGO_SETTINGS_MODULE': 'django_spicedham.settings'})
sys.path.insert(0, ROOT)

# This can't be imported until after we've fiddled with the
# environment.
from django.test.utils import setup_test_environment
setup_test_environment()

# Run nose.
#
# nose.run() returns True if tests passed and False otherwise which is
# the inverse of what we want the process to return, so we invert it.
sys.exit(not nose.run())
