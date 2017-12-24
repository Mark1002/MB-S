FROM python:3
MAINTAINER mark chang <ak0922747401@gmail.com>

WORKDIR /MB-S

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["sh", "-c", "cd mb_s && python manage.py runserver 0.0.0.0:8000"]