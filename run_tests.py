#!/usr/bin/env python

import os
import sys

import nose


# Set up the environment for our test project.
ROOT = os.path.abspath(os.path.dirname(__file__))

os.environ.update({'DJANGO_SETTINGS_MODULE': 'test_settings'})
# import to check for the existence of Django
import django
from django.core.management import call_command
from django.db import models
from spicedham.contrib.spicedham.models import Store
models.register_models('spicedham', Store)
call_command('syncdb', interactive=False)
sys.path.insert(0, ROOT)

import pdb
pdb.set_trace()
# This can't be imported until after we've fiddled with the
# environment.
from django.test.utils import setup_test_environment
setup_test_environment()

# Run nose.
#
# nose.run() returns True if tests passed and False otherwise which is
# the inverse of what we want the process to return, so we invert it.
sys.exit(not nose.run())
