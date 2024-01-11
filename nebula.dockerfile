FROM python:3.11-slim

WORKDIR /nebula

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV TZ = Asia/Seoul

RUN mkdir -p /var/log/nebula_server

COPY ./deploy/nebula_server.conf /etc/supervisor/conf.d/

EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8001"]
