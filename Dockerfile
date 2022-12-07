FROM python:3.11-slim
COPY requirements.txt .
COPY main.py .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python", "main.py"]
