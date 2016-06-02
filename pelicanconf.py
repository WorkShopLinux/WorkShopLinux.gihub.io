#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '2TRCA'
SITENAME = 'Workshop Linux'
SITEURL = 'http://workshoplinux.github.io/'
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
LINKS = (('Debian', 'http://workshoplinux.github.io/2016/04/linux-debian/'),
         ('RedHat', 'http://workshoplinux.github.io/2016/04/linux-redhat-enterprise/'),
         ('Suse', 'http://workshoplinux.github.io/2016/04/linux-suse-enterprise/'))
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
SITE_THUMBNAIL = 'https://app.box.com/representation/file_version_65462663706/image_2048/1.png?shared_name=spnjqjkijy2bss0q3blf8vzuyu9agsqy'
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
FAVICON = 'https://app.box.com/representation/file_version_65462663706/image_2048/1.png?shared_name=spnjqjkijy2bss0q3blf8vzuyu9agsqy'
ICON = 'https://app.box.com/representation/file_version_65462663706/image_2048/1.png?shared_name=spnjqjkijy2bss0q3blf8vzuyu9agsqy'
SHORTCUT_ICON = 'https://app.box.com/representation/file_version_65462663706/image_2048/1.png?shared_name=spnjqjkijy2bss0q3blf8vzuyu9agsqy'
HEADER_IMAGE = 'https://app.box.com/representation/file_version_65461344342/image_2048_jpg/1.jpg?shared_name=30mljt84zaggnmkhhbug3oq25j3ariqt'
BACKGROUND_IMAGE = 'https://app.box.com/representation/file_version_65462663706/image_2048/1.png?shared_name=spnjqjkijy2bss0q3blf8vzuyu9agsqy'
COPYRIGHT = '<a href="https://travis-ci.org/WorkShopLinux/WorkShopLinux.github.io"><img src="https://travis-ci.org/WorkShopLinux/WorkShopLinux.github.io.svg?branch=pelican"></a> | 2016 &copy; Todos direitos reservados.<script>'
PERSONAL_PHOTO = 'https://app.box.com/representation/file_version_65458744990/image_2048/1.png?shared_name=a88v0lhutyg6a5uqpjtbgrqriv758wda'
PERSONAL_INFO = 'Nós somos a turma do segundo ano do curso superior tecnológico de redes de computadores, somos amantes de software livre e das filosofias GNU e Open source.<p>Motivados pela elaboração de uma workshop explanando nossos conhecimentos e vivencias no ambiente Linux, este blog  foi criado para divulgar ainda mais o conhecimento e as possibilidades que os sistemas Open Source existentes no mercado atual podem  nos oferecer.'
NAV_LINK_NAME_DROP = '''<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5QPCMF"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5QPCMF');</script>
<!-- End Google Tag Manager -->distribuições'''
NAV_LINK_2 = 'SOBRE'
NAV_LINK_3 = 'BLOG'
NAV_LINK_4 = 'TRABALHOS'
TI_LINK_4 = 'Trabalhos'
TI_LINK_3 = 'Distribuições\n'
DESC_LINK_3 = 'Alguma das distribuições abordadas'
NOME_BT_ART = 'Ler'
TI_LINK_2 = 'A equipe'
TX_MORE = 'Veja mais'
TX_COM = ' Comentários'
TX_COM_1 = ' Comentários'
BT_NXT = ' Próximo'
BT_OD = ' Voltar'
CONT_RELA = 'Conteudo Relacionado' #caso plugin coment esteja ligado
ARTICLES_HOME_PAGE = False #só colocar True caso queira que a home seja os artigos
TI_LINK_4 = 'Agradecimentos\n'
TI_01 = 'Coolaboradores'
TI_02 = '2TRCA e #ROOT'
TI_03 = 'FIAP'
CO_01 = '<a href="http://z4yon.github.io/">Victor Apolonio</a> - Desenvolvedor<p>Professor Fábio Cabrini - Responsavel</p>'
CO_02 = 'A turma TRCA, pela iniciativa de disponibilizar o resultado de suas pesquisasas. A equipe #ROOT por manter o conteudo do blog.'
CO_03 = 'Disponibilização do espaço para a workshop.'
