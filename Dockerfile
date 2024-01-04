FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt


EXPOSE 8002

CMD ["uvicorn", "route:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
