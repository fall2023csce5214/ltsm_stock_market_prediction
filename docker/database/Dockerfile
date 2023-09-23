FROM postgres:latest

WORKDIR /database

COPY ./ddl/stocks.sql /docker-entrypoint-initdb.d

RUN apt update -y

RUN apt install procps -y