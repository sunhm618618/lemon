import os
# print('0',__file__)  #  python  文件.py
# print('1',os.path.abspath(__file__))
# print('2',os.path.dirname(os.path.abspath(__file__)))
# print('3',os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目跟目录
CASE_DIR = os.path.join(BASE_DIR, 'testcases')  # 用例脚本所在目录
DATA_DIR = os.path.join(BASE_DIR, 'data')  # 用例数据目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')  # 配置文件路径
DRIVER_DIR = os.path.join(BASE_DIR,'driver')  # 配置文件路径

REPORT_DIR = os.path.join(BASE_DIR, 'reports')  # 测试报告路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')  # 日志目录路径
CONF_FILE = os.path.join(CONF_DIR,'config.ini')  # 配置文件路径
DRIVER = os.path.join(DRIVER_DIR, 'chromedriver')  # 配置文件路径

if __name__ == '__main__':
    print('项目路径是:', BASE_DIR)
    print('用例脚本保存在：', CASE_DIR)
    print('数据保存在：', DATA_DIR)
    print('报告保存在：', REPORT_DIR)
    print('日志保存在：', LOG_DIR)
    print("driver保存在：",DRIVER)
