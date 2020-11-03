FROM postgres

RUN apt update \
    && apt install -y curl 

COPY ./ /home/pg/

WORKDIR /home/pg

EXPOSE 5432

CMD ./loading_sql.sh
