#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'KU Leuven neuromechanics group'
SITENAME = 'KUL Neuromechanics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Specify a customized theme, via absolute path
#THEME = "C:/Users/u0088756/Documents/Software/WebPage/PelicanThemesGit/~/pelican-themes/blueidea"

# Blogroll
LINKS = (('Github', 'https://github.com/MaartenAfschrift/'),('KU Leuven HBM','https://gbiomed.kuleuven.be/english/research/50000737/groups/HMB'))
GITHUB_URL = 'https://github.com/MaartenAfschrift/'

ABOUT_ME = 'Biomechanics, neural control, muscloskeletal modelling.'
AVATAR = 'images/TempPicture.jpg'

# Social widget
SOCIAL = ()
DEFAULT_PAGINATION = 2

# Pages
DISPLAY_PAGES_ON_MENU = True 
STATIC_PATHS = [
    'images',
	'html',
]

READERS = {'html': None}

#Second theme
THEME = '../Themes'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['C:/Users/u0088756/Documents/Software/WebPage/pelican-plugins'] 
PLUGINS = ['i18n_subsites']

LINKS_WIDGET_NAME = 'Research'
