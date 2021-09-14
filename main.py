import webapp2
import sys
import json

sys.path.append('modules')
from paste import httpserver
from base_handler import BaseHandler
from webhook_imobzi import WebhookHandlers, WebhookWithImobzi
from contact_utils import ContactModule
from webhook import Webhook

class Index(BaseHandler):
    """Index"""

    def get(self):
        """Get App Index"""
        # WebhookWithImobzi().get_devolus()
        # WebhookWithImobzi().create_webhook()
        WebhookWithImobzi().update_webhook('6403758877573120')
        # WebhookWithImobzi().update_webhook('4618263889707008')
        # WebhookWithImobzi().get_webhook('6403758877573120')
        # WebhookWithImobzi().get_all_webhook()
        # WebhookWithImobzi().delete_webhook('6208469986181120')
        # WebhookWithImobzi().delete_all_webhook([6403758877573120])
        self.response_send({"API": "New API"})

    def post(self):
        self.log_request_post()

app = webapp2.WSGIApplication([
    webapp2.Route('/v1',
        handler=Index,
        name='home'),
    webapp2.Route(
        '/v1/contact/<person_id>', 
        handler=ContactModule,
        name='home'),
    webapp2.Route(
        '/v1/webhook/imobzi', 
        handler=WebhookHandlers,
        name='webhookImobzi'),
    webapp2.Route(
        '/v1/imobzi/files', 
        handler=ContactModule,
        name='imobzi-files',
        methods=['GET', 'POST', 'OPTIONS']),
    webapp2.Route(
        '/v1/webhhok/pjbank', 
        handler=Webhook,
        name='imobzi-files'),
], debug=True)

def main():
    httpserver.serve(app, host='0.0.0.0', port='8050')
    # httpserver.serve(app, host='127.0.0.1', port='8050')

if __name__ == '__main__':
    main()