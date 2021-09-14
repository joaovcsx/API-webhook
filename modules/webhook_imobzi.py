#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from base_handler import BaseHandler


HEADERS = {
    'Accept': 'application/json',
    'Content-type':'application/json',
    'X-Imobzi-Secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aGlyZF9wYXJ0eV9hcHBfaWQiOjcwNjYyNjk3NywiY3JlYXRlZF9hdCI6IjIwMjEtMDctMTlUMTg6MDM6NDEuNDk1NDM1WiIsImlzX3RoaXJkX3BhcnR5X2FjY2VzcyI6dHJ1ZX0.2qXucHP9hVJGbLyMLgEtOF9CH6FQmOmhQBDc5ykOghs'
}

API = 'https://api.imobzi.app/v1'
NGROK_URL = 'https://f299a85d700c.ngrok.io/v1'
# API = 'http://localhost:8080/v1'
# NGROK_URL = 'http://localhost:8050/v1'
EVENTS = ['lead_created', 'lead_updated', 'lead_deleted',
          'contact_created', 'contact_updated', 'contact_deleted',
          'property_created', 'property_updated', 'property_deleted']

class WebhookHandlers(BaseHandler):

    def get(self):
        self.logging_request()

    def post(self):
        self.logging_request()

class WebhookWithImobzi(BaseHandler):

    def get_devolus(self):
        """Get Devolus"""
        url = 'https://api.devolusvistoria.com.br/api/vistorias/imoveis/199990'
        headers = {
            'User-Agent': 'python-requests/2.17.3',
            'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
            'Authorization': 'Bearer 395a92d0-d82d-487f-82a9-652a375db39a',
            'Connection': 'keep-alive'
        }
        request = requests.get(url, headers=headers)
        self.logging_response(request)

    def create_webhook(self):
        """Create webhook"""
        try:
            data = {'events': EVENTS, 'url': NGROK_URL + '/webhook/imobzi'}
            request = requests.post(API + '/webhooks', json=data, headers=HEADERS)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)

    def update_webhook(self, webhook_id):
        """"Update webhook default {u'db_id': 6403758877573120}"""
        try:
            data = {
                'events': EVENTS,
                'url': NGROK_URL + '/webhook/imobzi',
                'authorization': 'X-Imobzi-Authorization-Test'
            }
            url = API + '/webhook/{}'
            request = requests.post(url.format(webhook_id), json=data, headers=HEADERS)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)

    def get_webhook(self, webhook_id):
        try:
            url = API + '/webhook/{}'
            request = requests.get(url.format(webhook_id), headers=HEADERS)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)

    def get_all_webhook(self):
        try:
            url = API + '/webhooks'
            request = requests.get(url, headers=HEADERS)
            self.logging_response(request)
            return self.get_content(request)
        except Exception as error:
            self.logging_error(error)

    def delete_webhook(self, webhook_id):
        try:
            url = API + '/webhook/{}'
            request = requests.delete(url.format(webhook_id), headers=HEADERS)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)

    def delete_all_webhook(self, webhooks_ids):
        webhooks = self.get_all_webhook()
        for webhook in webhooks:
            if webhook['db_id'] not in webhooks_ids:
                self.delete_webhook(webhook['db_id'])