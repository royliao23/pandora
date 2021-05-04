FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d


RUN mkdir -p /home/django_test
RUN mkdir /home/django_test/static
WORKDIR /home/django_test/static/
#COPY ./static/ .
