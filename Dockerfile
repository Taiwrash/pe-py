FROM python:3.11.14-alpine

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY src app

CMD ["python3", "/app/app.py"]