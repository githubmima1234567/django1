# Scrapy settings for zhenai project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zhenai"

SPIDER_MODULES = ["zhenai.spiders"]
NEWSPIDER_MODULE = "zhenai.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    # "Accept-Language": "en",
# "Host": "www.zhenai.com",
# "Connection": "keep-alive",
# "Content-Length": "271",
# "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
# "Accept": "application/json, text/plain, */*",
# "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
# "sec-ch-ua-mobile": "?0",
# "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
# "sec-ch-ua-platform": "\"Windows\"",
# "Origin": 'https://www.zhenai.com',
# "Sec-Fetch-Site": "same-origin",
# "Sec-Fetch-Mode": "cors",
# "Sec-Fetch-Dest": "empty",
# "Cookie": "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zhenai.middlewares.ZhenaiSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zhenai.middlewares.ZhenaiDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "zhenai.pipelines.ZhenaiPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
