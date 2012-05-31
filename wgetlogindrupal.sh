#!/bin/bash

echo -n "Site name (URL including trailing slash): "
read -e SITE
read -p "Username: " USERNAME
read -p "Password: " -s PASSWORD
COOKIES=/tmp/drupalcron-cookies.txt

touch $COOKIES
echo -n
echo -n
wget -O /dev/null --save-cookies $COOKIES --keep-session-cookies --load-cookies $COOKIES "${SITE}user"
echo -n
wget --keep-session-cookies --save-cookies $COOKIES --load-cookies $COOKIES -O /dev/null \
        --post-data="name=$USERNAME&pass=$PASSWORD&op=Log%20in&form_id=user_login" \
        "${SITE}user?destination=login_redirect"
echo -n
wget --keep-session-cookies --save-cookies $COOKIES --load-cookies $COOKIES "${SITE}login_redirect"
