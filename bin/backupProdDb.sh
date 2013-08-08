#!/bin/bash

heroku pgbackups:capture --app ravenskeepchars

wget `heroku pgbackups:url --app ravenskeepchars`

