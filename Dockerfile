FROM python:latest

RUN apt-get update && apt-get install -y wget unzip gnupg2

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list

# Update and install Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable
WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . .

EXPOSE 8004

CMD ["./main.sh"]
