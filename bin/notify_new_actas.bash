#!/bin/bash
echo "hola"
source /home/constitucionabierta/constitucion-abierta-test/constitucionabiertaenv/bin/activate && python /home/constitucionabierta/constitucion-abierta-test/manage.py notify_new_actas 

