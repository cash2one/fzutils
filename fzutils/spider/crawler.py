# coding:utf-8

'''
@author = super_fazai
@File    : crawler.py
@connect : superonesfazai@gmail.com
'''

"""
爬虫基类
"""

from logging import INFO, ERROR
from gc import collect
from asyncio import (
    get_event_loop,
)

from ..ip_pools import (
    fz_ip_pool,
    ip_proxy_pool,)
from ..internet_utils import (
    get_random_pc_ua,
    get_random_phone_ua,)
from ..log_utils import set_logger
from ..time_utils import get_shanghai_time
from .fz_phantomjs import (
    BaseDriver,
    CHROME,
    PHANTOMJS,)
from ..safe_utils import get_uuid1

__all__ = [
    'Crawler',          # 爬虫基类
    'AsyncCrawler',     # 异步爬虫
]

# user_agent_type
PC = 'PC'
PHONE = 'PHONE'

class Crawler(object):
    def __init__(self,
                 ip_pool_type=ip_proxy_pool,
                 user_agent_type=PC,
                 log_print=False,
                 logger=None,
                 log_save_path=None,
                 
                 # driver设置
                 is_use_driver=False,
                 driver_executable_path=None,
                 driver_type=PHANTOMJS,
                 driver_load_images=False,
                 headless=False,
                 driver_obj=None,
                 driver_cookies=None,):
        '''
        :param ip_pool_type: 使用ip池的类型
        :param user_agent_type:
        :param log_print: bool 打印类型是否为log/sys.stdout.write
        :param log_save_path: log文件的保存路径
        :param is_use_driver: 是否使用驱动
        :param driver_executable_path: 驱动path
        '''
        super(Crawler, self).__init__()
        self.ip_pool_type = ip_pool_type
        self.user_agent_type = user_agent_type
        self._set_headers()
        # TODO logger name 都统一为self.lg
        self.lg = logger
        if log_print:
            self.log_save_path = log_save_path
            self._set_logger()
        if is_use_driver:
            self.is_use_driver = is_use_driver
            # TODO 名字统一都为self.driver, 避免内存释放错误
            self.driver = BaseDriver(
                type=driver_type,
                load_images=driver_load_images,
                executable_path=driver_executable_path,
                logger=self.lg,
                headless=headless,
                user_agent_type=user_agent_type,
                driver_obj=driver_obj,
                ip_pool_type=ip_pool_type,
                driver_cookies=driver_cookies,)

    def _set_headers(self) -> None:
        '''
        headers初始化
        :return:
        '''
        self.headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': get_random_pc_ua() if self.user_agent_type == PC else get_random_phone_ua(),
            'accept': '*/*',
        }

    def _set_logger(self) -> None:
        '''
        logger初始化
        :return:
        '''
        self.lg = set_logger(
            log_file_name=self.log_save_path + str(get_shanghai_time())[0:10] + '.txt',
            console_log_level=INFO,
            file_log_level=ERROR
        ) if self.lg is None else self.lg

    def __del__(self):
        '''
        释放
        :return:
        '''
        # 分开释放, 避免出错, 内存溢出
        def del_headers() -> None:
            try:
                del self.headers
            except:
                pass

        def del_logger() -> None:
            try:
                del self.lg
            except:
                pass

        def del_driver() -> None:
            if self.is_use_driver:
                try:
                    del self.driver
                except:
                    pass

        del_headers()
        del_logger()
        del_driver()
        collect()

class AsyncCrawler(Crawler):
    """异步crawler"""
    def __init__(self, *params, **kwargs):
        '''
        :param ip_pool_type: ip池类型
        :param log_print: bool 打印类型是否为log/sys.stdout.write
        :param logger:
        :param log_save_path: 日志存储路径
        '''
        Crawler.__init__(self, *params, **kwargs)
        self.loop = get_event_loop()
        self.concurrency = 9            # 控制并发量

    async def _get_phone_headers(self):
        pass

    async def _get_pc_headers(self):
        pass

    async def _get_new_logger(self, logger_name=get_uuid1()):
        '''
        获取一个新的日志对象
        :param logger_name:
        :return:
        '''
        assert self.log_save_path != '', 'log_save_path为空值!'

        return set_logger(
            log_file_name=self.log_save_path + str(get_shanghai_time())[0:10] + '.txt',
            logger_name=logger_name,
            console_log_level=INFO,
            file_log_level=ERROR)

    async def _fck_run(self):
        pass

    def __del__(self):
        try:
            del self.loop
        except:
            pass
        collect()
