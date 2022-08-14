FROM python:3.9-slim as builder

RUN apt update && apt upgrade -y
RUN pip3 install pipenv

RUN useradd -m app

WORKDIR /home/app
COPY Pipfile ./
RUN chown -R app /home/app
USER app

# packageコマンドなどシステムにインストール
RUN pipenv install --deploy && pipenv install --system

# python3.9.2 nonroot 
FROM gcr.io/distroless/python3@sha256:7f0f41349f78f1ebc321eb28e3679e7bc64e5d6348cf6d524e06b8777751839a
# gunicornなどのpython由来のコマンドをコピー
COPY --from=builder /home/app/.local/bin/ /home/nonroot/.local/bin/
COPY --from=builder /home/app/.local/lib/python3.9/site-packages/ /home/nonroot/.local/lib/python3.9/site-packages/
COPY . /home/nonroot
USER nonroot

EXPOSE 8080
CMD ["/home/nonroot/.local/bin/gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "--config", "./gunicorn-cfg.py"]
