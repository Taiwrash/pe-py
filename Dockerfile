FROM python:3.11.14-alpine

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src app

CMD ["python3", "/app/app.py"]