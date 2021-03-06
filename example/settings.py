# -*- coding: utf-8 -*-

# Scrapy settings for example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent


USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html


# -------------splash相关配置-----------------------------------------------
# splash render.html端点地址
SPLASH_URL = "http://localhost:8050"
# splash 去重过滤器，具体是过滤什么的我也不晓得。。。
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
# 用来支持SplashRequest中的cache_args参数的配置
SPIDER_MIDDLEWARES = {
   # 'example.middlewares.ExampleSpiderMiddleware': 543,
   'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}


DOWNLOADER_MIDDLEWARES = {
   #　因为默认系统的CookiesMiddleware是开始的，所以我们重用并且赋值为None,让他失效
   'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':None,
   'example.middlewares.CustomerCookiesMiddleware':701,
   # 下面三个是对应splash的相关配置

   "scrapy_splash.SplashCookiesMiddleware":723, # 开启相关scrapy_splash中间件
   "scrapy_splash.SplashMiddleware":725, # 开启相关scrapy_splash中间件
   # 调整系统scrapy内部中间件的顺序
   "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware":810,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'example.pipelines.ExamplePipeline': 300,
   # 'example.pipelines.MYSQLPipeline': 301,
   # 处理文件下载的内置pipelien插件
   # 'scrapy.pipelines.files.FilesPipeline':1,
   # 继承FilesPipeline改写文件路径生成函数的文件保存pipeline
   # 'example.pipelines.MyFilesPipeline':1,
   # 图片处理内置pipeline
   'scrapy.pipelines.images.ImagesPipeline':1,
}

# 当使用FilesPipeline的时候的配合用法，指定下载的文件的文件夹路径保存地址
FILES_STORE = 'example_src'
# 当使用FImagesPipeline的时候的配合用法，指定下载的文件的文件夹路径保存地址

IMAGES_STROE = 'download_images'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
