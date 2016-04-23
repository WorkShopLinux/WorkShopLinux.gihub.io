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
LINKS = (('Debian', 'http://workshoplinux.github.io/2016/03/linux-debian/'),
         ('Open Suse', 'http://workshoplinux.github.io/2016/03/linux-open-suse/'),
         ('RedHat', 'http://workshoplinux.github.io/2016/03/linux-redhat/'))
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
HEADER_IMAGE = 'https://app.box.com/representation/file_version_65461344342/image_2048_jpg/1.jpg?shared_name=30mljt84zaggnmkhhbug3oq25j3ariqt'
BACKGROUND_IMAGE = 'http://www.clipartbest.com/cliparts/nTE/GRq/nTEGRqGTA.png'
COPYRIGHT = '<a href="https://travis-ci.org/WorkShopLinux/WorkShopLinux.github.io"><img src="https://travis-ci.org/WorkShopLinux/WorkShopLinux.github.io.svg?branch=pelican"></a> | 2016 &copy; Todos direitos reservados<a href="http://z4yon.github.io/">.</a>'
PERSONAL_PHOTO = 'https://app.box.com/representation/file_version_65458744990/image_2048/1.png?shared_name=a88v0lhutyg6a5uqpjtbgrqriv758wda'
PERSONAL_INFO = 'entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre entre aqui com o texto da parte sobre '
NAV_LINK_NAME_DROP = 'distribuições'
NAV_LINK_2 = 'SOBRE'
NAV_LINK_3 = 'BLOG'
NAV_LINK_4 = 'TRABALHOS'
TI_LINK_4 = 'Trabalhos'
TI_LINK_3 = 'Distribuições'
DESC_LINK_3 = '\nAlguma das distribuições abordadas'
NOME_BT_ART = 'Ler'
TI_LINK_2 = 'A equipe'
TX_MORE = 'Veja mais'
TX_COM = 'Comentários'
TX_COM_1 = 'Comentários'
BT_NXT = 'Próximo'
BT_OD = 'Voltar'
CONT_RELA = 'Conteudo Relacionado' #caso plugin coment esteja ligado
ARTICLES_HOME_PAGE = False #só colocar True caso queira que a home seja os artigos
