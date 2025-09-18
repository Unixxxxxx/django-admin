FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput
RUN pip install gunicorn

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

