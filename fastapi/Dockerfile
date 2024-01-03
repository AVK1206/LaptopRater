FROM python:latest

WORKDIR /app

COPY ../ .

RUN pip install selenium beautifulsoup4 pymongo fastapi uvicorn


EXPOSE 8000

CMD ["uvicorn", "route:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
