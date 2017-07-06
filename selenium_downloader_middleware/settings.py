# -*- coding: utf-8 -*-

BOT_NAME = 'selenium_downloader_middleware'

SPIDER_MODULES = ['selenium_downloader_middleware.spiders']
NEWSPIDER_MODULE = 'selenium_downloader_middleware.spiders'

DOWNLOADER_MIDDLEWARES = {
    'selenium_downloader_middleware.middlewares.SeleniumMiddleware': 723,
}

ROBOTSTXT_OBEY = False
