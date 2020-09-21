import webapp2
import sys

sys.path.append('modules')
from base_handler import BaseHandler
from webhook_imobzi import WebhookHandlers, WebhookWithImobzi
from contact_utils import ContactModule
from webhook import Webhook

class Index(BaseHandler):
    """Index"""

    def get(self):
        """Get App Index"""
        # WebhookWithImobzi().create_webhook()
        WebhookWithImobzi().update_webhook('6403758877573120')
        # WebhookWithImobzi().get_webhook('5646433661222912')
        # WebhookWithImobzi().get_all_webhook()
        # WebhookWithImobzi().delete_webhook('6208469986181120')
        # WebhookWithImobzi().delte_all_webhook([6403758877573120])
        self.response_send({"API": "Aprendendo a construir uma API"})


app = webapp2.WSGIApplication([
    webapp2.Route('/v1', handler=Index, name='home'),
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
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8050')

if __name__ == '__main__':
    main()