# Scrapy settings for proxy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'proxy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['proxy.spiders']
NEWSPIDER_MODULE = 'proxy.spiders'

USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOAD_DELAY = 0
DOWNLOAD_TIMEOUT = 30

ITEM_PIPELINES = [
    'proxy.pipelines.ProxyPipeline'        
]

CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS_PER_SPIDER = 64
CONCURRENT_SPIDERS = 128

LOG_ENABLE = True
LOG_ENCODING = 'utf-8'
LOG_FILE = '/home/eric/workspace/python/proxy/log/proxy.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False