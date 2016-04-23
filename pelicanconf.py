#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '2TRCA'
SITENAME = 'Workshop Linux'
SITEURL = ''
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
PATH = 'content'
WITH_FUTURE_DATES = False
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False
LINKS = (('Debian', 'http://pudim.com.br'),
         ('Open Suse', 'http://google.com/'),
         ('RedHat', 'http://google.com/'))
SOCIAL = (
          
          
          
          )
DEFAULT_PAGINATION = True
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')
POST_LIMIT = 3
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'neighbors', 'related_posts']
THEME = "theme_flat"
SWIFTYPE = ''
SITE_THUMBNAIL = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
SITE_THUMBNAIL_TEXT = 'Vamos falar de Linux'
SITESUBTITLE = ''
DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = ''
GOOGLE_ANALYTICS_DOMAIN = ''
RELATED_POSTS_MAX = 20
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
FAVICON = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
ICON = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
SHORTCUT_ICON = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
HEADER_IMAGE = 'http://www.sinestec.com.br/wp-content/uploads/2015/03/data_center.jpg'
BACKGROUND_IMAGE = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
COPYRIGHT = '2016 &copy; Todos direitos reservados.'
PERSONAL_PHOTO = "https://cnet2.cbsistatic.com/hub/i/r/2015/05/31/3d97705c-8ea1-4030-ac30-193b4b22d9a7/resize/570xauto/e738e2b3a5b3dacc1fade21d2dd6524a/twitch-kappa.jpg"
