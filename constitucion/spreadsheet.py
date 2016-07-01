# -*- coding: UTF-8 -*-.

from __future__ import print_function
import argparse
import sqlite3
import time
import hashlib
import sys
import random


from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


SHEET_ID = settings.SPREADSHEET_ID

def insert(number, acta_id, acta_url, acta_modificar_url, encargado):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name(settings.SERVICEKEY, SCOPES)
    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    data = {'values': [[acta_id, acta_url, acta_modificar_url, '', encargado]]}

    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='datos!A%s' % number, body=data, valueInputOption='RAW'
    ).execute()

def set_modified(number, acta_url, acta_modificar_url):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    creds = ServiceAccountCredentials.from_json_keyfile_name(settings.SERVICEKEY, SCOPES)
    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

    data = {'values': [[acta_url, acta_modificar_url, 'TRUE']]}

    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='datos!B%s' % number, body=data, valueInputOption='RAW'
    ).execute()

