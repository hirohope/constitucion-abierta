#!/bin/bash

NAME="constitucion_abierta.app"                                  # Name of the application
DJANGODIR=/Users/hope/constitucion_abierta             # Django project directory
SOCKFILE=/Users/hope/constitucion_abierta/run/gunicorn.sock  # we will communicte using this unix socket
USER=hope                                        # the user to run as
GROUP=staff                                     # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=constitucion_abierta.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=constitucion_abierta.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /Users/hope/.virtualenvs/constitucion/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
# RUNDIR=$(dirname $SOCKFILE)
# test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-