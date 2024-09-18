# 使用 Python 3.9 slim 版本作为基础镜像
FROM python:3.9-slim

# 设置时区
# RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# RUN echo "Asia/Shanghai" | tee /etc/timezone

# 设置工作目录
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "main.py"]
# docker run -d --name weather-server -v ./logs/http_server.log:/app/logs/http_server.log -e PYTHONUNBUFFERED=1 weather-server
