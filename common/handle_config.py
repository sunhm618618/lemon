from configparser import ConfigParser
from common.handle_path import CONF_FILE


class ConfigHandler(ConfigParser):
    """用于读取配置文件的处理程序"""

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf8')


conf = ConfigHandler(CONF_FILE)
if __name__ == '__main__':
    conf = ConfigHandler(CONF_FILE)
    print(conf['mysql']['port'])
    print(conf['mysql']['user'])
    print(conf['test_data']['phone'])
