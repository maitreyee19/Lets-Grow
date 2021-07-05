FROM python:3.8.3-slim

# set working dir
WORKDIR /apps

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc && pip3 install --upgrade pip
COPY ./requirements.txt /apps/
RUN pip install -r requirements.txt

# copy project
COPY ./main /apps/main
COPY ./application.py /apps/
COPY ./google-oidc.json /apps/


# CMD ["/bin/sh"]
CMD ["waitress-serve", "--call" , "application:create_app"]