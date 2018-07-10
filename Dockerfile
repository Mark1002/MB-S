FROM python:3
LABEL mark chang <ak0922747401@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /MB-S
WORKDIR /MB-S
COPY . /MB-S
RUN mkdir /MB-S/mb_s/log
RUN pip install -r requirements.txt
