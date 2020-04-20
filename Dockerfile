FROM python:3.7-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "dsw_netilion_client.py"]

#
# docker build -t dsw_benchmark .
# docker run --rm -p 9090:9090 dsw_benchmark
#
# powershell -Command "docker ps -q | % { docker stop $_ }"