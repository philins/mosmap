#!/bin/sh

MYID="114012108"
MSMP="-241542988"

message(){
m=$@
curl -s -X POST https://api.telegram.org/bot516537755:AAFXv4iODt8--_3HUjAbr28QJP82JMrPu9A/sendMessage -d chat_id=$MYID -d text="$m"  -d "parse_mode=markdown" -d "disable_web_page_preview=true"
}

#message Docker started
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