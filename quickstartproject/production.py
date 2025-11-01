from .settings import *
import os

# Configure ALLOWED_HOSTS with this priority:
# 1. Use a comma-separated ALLOWED_HOSTS environment variable if provided.
# 2. Always include the Azure WEBSITE_HOSTNAME (the *.azurewebsites.net host).
# This lets you add custom domains either by setting ALLOWED_HOSTS in App
# Settings (recommended) or by editing this file to include specific hosts.
env_allowed = os.environ.get('ALLOWED_HOSTS', '')
hosts = [h.strip() for h in env_allowed.split(',') if h.strip()]

if 'WEBSITE_HOSTNAME' in os.environ and os.environ['WEBSITE_HOSTNAME'] not in hosts:
	hosts.append(os.environ['WEBSITE_HOSTNAME'])

ALLOWED_HOSTS = hosts

DEBUG = False
