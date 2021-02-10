#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from base_handler import BaseHandler


HEADERS = {
    'Accept': 'application/json', 
    'Content-type':'application/json',
    'X-Imobzi-Secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aGlyZF9wYXJ0eV9hcHBfaWQiOjU4NTk0MDMyMSwiY3JlYXRlZF9hdCI6IjIwMjAtMDctMjhUMTc6NDk6NDQuOTUzMjcyWiIsImlzX3RoaXJkX3BhcnR5X2FjY2VzcyI6dHJ1ZX0.BBW19UzLkNVYqDsm4-divx6o6A2aV4m4DQiiRIKE-8w'
}

API = 'https://api.imobzi.app/v1'
NGROK_URL = 'https://9931bf989512.ngrok.io/v1'

class WebhookHandlers(BaseHandler):
    
    def post(self):
        self.logging_request()

class WebhookWithImobzi(BaseHandler):

    def create_webhook(self):
        """Create webhook"""
        try:
            data = {
                'events': ['lead_updated', 'contact_updated', 'property_updated'],
                'url': NGROK_URL + '/webhook/imobzi'
            }
            url = API + '/webhooks'
            request = requests.post(url, json=data, headers=HEADERS)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)

    def update_webhook(self, webhook_id):
        """"Update webhook default {u'db_id': 6403758877573120}"""
        try:
            data = {
                'events': ['lead_created', 'lead_updated', 'lead_deleted', 
                    'contact_created', 'contact_updated', 'contact_deleted',
                    'property_created', 'property_updated', 'property_deleted'],
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
    
class PropertyPhotos(BaseHandler):
    
    def add_photos(self, property_id, data):
        try:
            url = API + '/properties/{}/photos'
            request = requests.post('http://127.0.0.1:8050/v1', headers=HEADERS, data=data)
            self.logging_response(request)
        except Exception as error:
            self.logging_error(error)