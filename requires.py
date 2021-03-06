# coding:utf-8

'''
@author = super_fazai
@File    : requires.py
@Time    : 2016/8/3 12:59
@connect : superonesfazai@gmail.com
'''

install_requires = [
    'ipython',
    'wheel',
    'utils',
    'db',
    'greenlet==0.4.14',     # 之前0.4.13, 改成0.4.14(gevent依靠)
    'web.py==0.40.dev1',
    'fake-useragent',       # 随机user-agent
    'pytz',
    'pysocks',              # requests 进行socks代理必备!
    'requests',
    'requests_oauthlib',
    # 'requests-html',        # requests的html解析器 for human, 但是必须python >= 3.6
    'selenium==3.8.0',      # 3.8.1及其以上版本不支持phantomjs了
    'uvloop',               # asyncio默认事件循环替代品
    'asyncio',
    'psutil',
    'pyexecjs',
    'setuptools',
    'colorama',
    'twine',
    'numpy',
    'pprint',
    'chardet',
    'bs4',
    'scrapy',
    'demjson',
    'pymssql',
    'sqlalchemy',
    'gevent',
    'aiohttp',
    'celery',
    'jsonpath',
    'matplotlib',
    'wget',
    'flask',
    'flask_login',
    'mitmproxy',            # shell 抓包代理
    'pymongo',
    'pyexcel',
    'pyexcel-xlsx',
    'fabric',
    'shadowsocks',
    # 'pycurl==7.43.0.1',
    'furl',
    'yarl',
    'prettytable',
    'xlrd',
    'pandas',
    'jieba',
    'geopandas',
    'scikit-image',
    'wordcloud',            # 词云
    'pygame',
    'appium-python-client',
    'python-docx',
    'Jinja2',
    'elasticsearch',
    'elasticsearch_dsl',
    'salt',                 # 为大规模复杂系统管理提供软件, 同步控制百万台服务器
    'ray',                  # 一个灵活的高性能分布式执行框架
    'jupyter',
    'ipywidgets',
    'bokeh',                # 一个用于Python的交互式可视化库，可在现代Web浏览器中实现美观且有意义的数据可视化呈现
    'stem',
    'pika',                 # RabbitMQ客户端库
    'redis',
    'flower',               # 一个基于Web的工具，用于监视和管理Celery集群。
    'items',
    'scapy',                # 功能强大的基于Python的交互式数据包操作程序和库
    'scapy-http',
    'baidu-aip',
    'pytesseract',
    'scrapy-splash',
    'opencv-python',
    'twilio',               # 免费发短信
    'fonttools',
    'xmltodict',
    'python-dateutil',
    'newspaper3k',          # 文章提取
    'ftfy',                 # 超级强大的unicode文本工具
    'tenacity',             # 强大的python重试库
    'pyzbar',               # 二维码识别库, 安装前提:(ubuntu: sudo apt-get install libzbar-dev | mac: brew install zbar)
    'eventlet',             # celery改变单个worker并发量必备库
    'termcolor',            # shell颜色化输出
    'Flask-APScheduler',    # flask的定时任务库
    'mongoengine',          # mongo engine
    'pypinyin',             # 汉字转拼音包
    # 'sip',
    # 'pyqt5',
]