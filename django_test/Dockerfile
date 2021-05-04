# pull official base image
FROM python:3.8.3-alpine
RUN mkdir -p /usr/src
RUN mkdir -p /home/django_test
RUN mkdir /home/django_test/static
RUN mkdir /home/django_test/media


# create the appropriate directories


# set work directory
WORKDIR /usr/src/django_test

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip

# install pillow
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./entrypoint.sh .

# copy project
COPY . .
# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
RUN chown -R app:app /usr/src/django_test
#WORKDIR $APP_HOME
# change owner of static folder to app
RUN chmod -R a+rwX /usr/src/django_test/static/
#RUN chown -R app:app /usr/src/django_test/static/
#RUN cp -r /usr/src/django_test/static/. /home/django_test/static
#RUN cp -r /usr/src/django_test/static/. /home/app/web/static
#RUN chmod -R 777 /home/app/web/static/
#RUN chmod -R 777 /usr/src/django_test/staticfiles/
RUN chown -R app:app /usr/src/django_test/static/
USER app
# run entrypoint.sh
#ENTRYPOINT ["/usr/src/django_test/entrypoint.sh"]
#ENTRYPOINT ["sh","/usr/src/django_test/entrypoint.sh"]

