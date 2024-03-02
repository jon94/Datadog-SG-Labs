FROM python:3.8
  
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["ddtrace-run", "gunicorn", "app:app", "-b", "0.0.0.0:5000"]