#!/bin/sh

curl -u $FTPUSER:$FTPPASS -O -k sftp://62.76.90.57/storage/www/moscowmap/moscowmap.ru/leaflet/postgis2.csv
curl -u $FTPUSER:$FTPPASS -O -k sftp://62.76.90.57/storage/www/moscowmap/moscowmap.ru/leaflet/postattr.sql
curl -u $FTPUSER:$FTPPASS -O -k sftp://62.76.90.57/storage/www/moscowmap/moscowmap.ru/leaflet/smallicons.sql
curl -u $FTPUSER:$FTPPASS -O -k sftp://62.76.90.57/storage/www/moscowmap/moscowmap.ru/leaflet/sobor.sql

sed -i 's/\.\.\/_public\///g' postattr.sql

psql -h pg -U postgres -d template_postgis -f mm_objects.sql
psql -h pg -U postgres -d template_postgis -c '\copy "public"."mm_objects" from postgis2.csv with (FORMAT CSV, DELIMITER "|");' > /dev/null 2>> err.log
psql -h pg -U postgres -d template_postgis -c "UPDATE mm_objects SET obj_name = replace(obj_name, '.', '') WHERE obj_st_id = '48'"
psql -h pg -U postgres -d template_postgis -c "UPDATE mm_objects SET obj_name = replace(obj_name, ' ', '') WHERE obj_st_id = '48'"
psql -h pg -U postgres -d template_postgis -f postattr.sql > /dev/null 2>> err.log
psql -h pg -U postgres -d template_postgis -f smallicons.sql > /dev/null 2>> err.log
psql -h pg -U postgres -d template_postgis -f sobor.sql > /dev/null 2>> err.log

cat err.log