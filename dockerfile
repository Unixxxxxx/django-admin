FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-chache-dir -r requirement.txt

COPY . .

RUN python manage.py collectstastic -noinput

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

