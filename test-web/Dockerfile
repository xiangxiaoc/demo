FROM python:3.9

RUN pip install "fastapi[standard]"

COPY . /app

WORKDIR /app

CMD ["fastapi", "dev", "web.py"]