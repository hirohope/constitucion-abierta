# -*- coding: UTF-8 -*-.

from __future__ import print_function
import argparse
import sqlite3
import time
import hashlib
import random

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def get_last_acta_number():

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"


    rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='no_modificar!A2').execute().get('values', [])
    last_row = int(rows[0][0])

    return last_row

def get_all_actas():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"

    rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='datos!H:H').execute().get('values', [])

    rows = [item for sublist in rows for item in sublist]

    return rows


def get_random_acta():

    rows = get_all_actas()
    row = random.choice(rows)
    row = row.replace('static/', '')

    return row


def is_valid_acta(acta_url, return_number = False):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"

    data = {'values': [[acta_url]]}
    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='no_modificar!B5', body=data, valueInputOption='RAW'
    ).execute()


    rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='no_modificar!B6').execute().get('values', [])
    is_valid = len(rows) > 0
    if is_valid:
        is_valid = rows[0][0] != "#N/A"

    if return_number:
        return rows[0][0] if is_valid else None
    else:
        return is_valid


def get_secret(acta_url):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"

    data = {'values': [[acta_url]]}
    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='no_modificar!B5', body=data, valueInputOption='RAW'
    ).execute()


    rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='no_modificar!B8').execute().get('values', [])
    if len(rows) > 0:
        secret = rows[0][0]
        rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='no_modificar!B7').execute().get('values', [])
        number = int(rows[0][0])
        return secret, number
    else:
        return None, None

def insert_new_acta(acta_url, acta_modificar_url, secret, encargado):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"


    rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='no_modificar!A2').execute().get('values', [])
    last_row = int(rows[0][0])
    new_row = last_row + 1

    data = {'values': [[new_row-1,acta_url, acta_modificar_url, '', encargado]]}

    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='datos!A%s' % new_row, body=data, valueInputOption='RAW'
    ).execute()

    data = {'values': [[secret]]}

    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='no_modificar!H%s' % new_row, body=data, valueInputOption='RAW'
    ).execute()

    return new_row-1

def insert(number, acta_url, acta_modificar_url):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"


    data = {'values': [[acta_url, acta_modificar_url]]}

    SHEETS.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range='datos!B%s' % number, body=data, valueInputOption='RAW'
    ).execute()


def check_in_spreadsheet(filename, secret):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
    SHEET_ID = "1tuovIOcBoZ7dx0N9wWrKG-O--hnX6wldA9WpiRmGxwc"

    real_secret, number = get_secret(filename)
    if real_secret == secret:
        return number
    else:
        return None
