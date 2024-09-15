# 使用 Python 3.9 slim 版本作为基础镜像
FROM python:3.9-slim

# 再次更新并安装 cron
RUN apt-get update && apt-get install -y cron

# 设置工作目录
WORKDIR /app

# 复制需求文件并安装 Python 包
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 将 Python 脚本和crontab文件复制到容器中
COPY your_script.py /app/your_script.py
COPY mycron /etc/cron.d/mycron

# 设置crontab文件的正确权限
RUN chmod 0644 /etc/cron.d/mycron

# 创建日志文件并设置权限
RUN touch /var/log/cron.log && chmod 0666 /var/log/cron.log

# 启动cron服务并持续运行
CMD ["cron", "-f"]
