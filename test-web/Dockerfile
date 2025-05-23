FROM python:3.9

RUN pip install "fastapi[standard]"

COPY . /app

WORKDIR /app

CMD ["fastapi", "dev", "--host", "0.0.0.0", "web.py"]