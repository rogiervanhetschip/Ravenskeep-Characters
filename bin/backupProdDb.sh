#!/bin/bash

mkdir -p ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`

heroku pg:credentials HEROKU_POSTGRESQL_GRAY_URL --app ravenskeepchars

#pg_dump -U $login -h $dbhost $database | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_FULL.sql.gz
#pg_dump -s -U $login -h $dbhost $database | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_SCHEMA.sql.gz
#pg_dump -a -U $login -h $dbhost $database | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_DATA.sql.gz

pg_dump -U -h | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_FULL.sql.gz
pg_dump -s -U -h | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_SCHEMA.sql.gz
pg_dump -a -U -h | gzip > ~/digi/ravenskeepCharsBackups/`date +\%Y\%m\%d`/ravenskeepChars_DATA.sql.gz


