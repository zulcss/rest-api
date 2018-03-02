from alpine:latest

run set -e && \
    apk add --no-cache python python-dev && \
    python -m ensurepip && \
    rm -rf /usr/lib/python*/ensurepip && \
    pip install --upgrade pip && \
    rm -rf /root/.cache

add . /app

workdir ./app
run pip install -r requirements.txt

entrypoint ["python", "app.py"]
