FROM python:3.6.5-slim-stretch

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY source source

CMD ["python", "-u", "source/pv.py"]
