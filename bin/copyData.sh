#!/bin/bash

if [ $# -lt 2 ]
then
  echo ERROR: Provide 2 of d, t, a and p. Source system first, target system second
  exit 1
fi

if [ $2 == 'p' ]
then
  echo WAAAAG! Be ye daft, ye cully?! No copyin\' to prod!
  exit 0
fi

typeset -A env
env[d]=dev
env[t]=ravenskeepcharstest
env[p]=ravenskeepchars

typeset -A db
db[d]=dev
db[t]=HEROKU_POSTGRESQL_DEV
db[p]=HEROKU_POSTGRESQL_GRAY

# 1. Source system (d, t, a, p)
SOURCE=${env[$1]}

# 2. Target system (d, t, a, p)
TARGET=${env[$2]}
TARGET_DATABASE=${db[$2]}

# 3. Dump of source system
if [ $SOURCE != 'dev' ]
then
  # Dump of heroku system
  echo Creating dump of $SOURCE
  #heroku pgbackups:capture --app $SOURCE --expire
else
  # Dump of dev
  echo TODO...
  exit 1
fi

# 4. Backup of target system
if [ $TARGET != 'dev' ]
then
  # Backup of heroku system
  echo Backup $TARGET
  #heroku pgbackups:capture --app $TARGET --expire
  # Restore this backup with `heroku pgbackups:restore HEROKU_POSTGRESQL_GRAY --app $TARGET`
else
  # Backup of dev
  echo TODO...
  exit 1
fi

# 5. Restore in target system
if [ $TARGET != 'dev' ]
then
  # Restore in heroku system
  echo Restoring on $TARGET to database $TARGET_DATABASE
  #heroku pgbackups:restore $TARGET_DATABASE `heroku pgbackups:url --app $TARGET`
else
  # Restore in dev
  echo TODO...
  exit 1
fi

# Dev? ../ravenskeepChars/settings.py, find 'NAME', 'USER' en 'PASSWORD'

