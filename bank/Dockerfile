FROM python:3.9
ENV PYTHONNUNBUFFERED 1
WORKDIR /app
COPY req.txt /app/req.txt   
RUN pip install -r req.txt 
COPY . /app