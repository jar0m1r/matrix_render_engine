FROM python:3.10.9-alpine3.17

ENV DEBIAN_FRONTEND=noninteractive
RUN apk update && apk add tmux

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
