import logging

# 创建第一个 logger
from logging.handlers import RotatingFileHandler

http_server_logger = logging.getLogger('http_server')
http_server_logger.setLevel(logging.DEBUG)  # 设置日志级别

# 创建处理器 handler，将日志输出到文件 .log
http_server_handler = RotatingFileHandler(
    'logs/http_server.log',
    maxBytes=5 * 1024 * 1024,  # 5MB，超过此大小会进行日志轮转
    backupCount=3  # 最多保留3个旧日志文件
)
http_server_handler.setLevel(logging.DEBUG)  # handler的日志级别

http_server_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
http_server_handler.setFormatter(http_server_formatter)  # 为 handler 添加格式

# 将 handler 添加到 logger
http_server_logger.addHandler(http_server_handler)

if __name__ == '__main__':
    http_server_logger.debug('This is a debug message from module1')
    http_server_logger.info('This is an info message from module1')
    http_server_logger.warning('This is a warning message from module2')
    http_server_logger.error('This is an error message from module2')
