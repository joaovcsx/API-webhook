#!/usr/bin/python
# -*- coding: utf-8 -*-

from base_handler import BaseHandler

class Webhook(BaseHandler):

    def post(self):
        print('\nPOST')
        request_dict = self.request.POST
        print(request_dict)
        print(self.request)
        print('\n')

    def put(self):
        print('\nPUT')
        request_dict = self.request_json()
        print(request_dict)
        print('\n')

    def delete(self):
        print('\nDELETE')
        request_dict = self.request.GET
        print(request_dict)
        print('\n')