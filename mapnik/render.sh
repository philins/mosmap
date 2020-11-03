#!/bin/sh
python prepare.py
python3 generate_t.py
mkdir ~/.ssh
ssh-keyscan -H $FTPHOST >> ~/.ssh/known_hosts 
sshpass -p $FTPPASS rsync --archive --verbose --progress tiles/ $FTPUSER@$FTPHOST:/storage/www/moscowmap/moscowmap.ru/htdocs/leafletnew/tiles/
python -m SimpleHTTPServer 8080