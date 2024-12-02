FROM nikolaik/python-nodejs:python3.12-nodejs20
WORKDIR /kanban_life
COPY . /kanban_life

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y ca-certificates curl gnupg libpango-1.0-0 libpangoft2-1.0-0
RUN apt-get update
RUN pip install poetry
RUN poetry install
RUN npm install -g pm2

