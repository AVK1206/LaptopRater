FROM python:latest

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . .

EXPOSE 8004

CMD ["./main.sh"]
