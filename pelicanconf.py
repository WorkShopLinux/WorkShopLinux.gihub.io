#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '2TRCA'
SITENAME = 'Workshop Linux'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['image',
                'static',
                'extra/sitelogo.png',
                'extra/favicon.ico',
                'extra/favicon.png',
                'extra/robots.txt',
            #    'extra/google331456191962689c',
                'extra/CNAME']
EXTRA_PATH_METADATA = {
                        'extra/sitelogo.png': {'path': 'sitelogo.png'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        'extra/favicon.ico': {'path': 'favicon.ico'},
                        'extra/favicon.png': {'path': 'favicon.png'},
                 #       'extra/google331456191962689c': {'path': 'google331456191962689c.html'},
                        'extra/CNAME': {'path': 'CNAME'},
                      }


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
