FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_DEBUG=False \
    PORT=8000

WORKDIR /app

COPY server/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt

COPY server/ /app/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh \
    && python manage.py collectstatic --noinput

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
