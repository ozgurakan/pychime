"""
Posts a message to Chime Chat Room using
the webhook
"""
import json
import requests

class ChimeException(Exception):
    """
    Exception Class for Chime
    """
    def __init__(self, code):
        super(ChimeException, self).__init__()
        self.code = code
        if code == 429:
            self.message = 'The incoming webhook rate limit exceeded'
        elif code == 413:
            self.message = 'Messages posted by the webhook is bigger than 16k'
        elif code == 404:
            self.message = 'Webhook for the chat room is deleted or regenerated'
        elif code == 403:
            self.message = 'Invalid webhook URL'
        elif code == 503:
            self.message = 'Service is unavailable'
        else:
            self.message = 'Could not post the message to the Chime Chat Room'

class Chime():
    """
    Manages Chime Chat Room Web-Hook
    """
    def __init__(self, webhook):
        self._webhook = webhook

    def post(self, message):
        """ Sends the message """
        payload = {
            'Content-Type' :'application/json',
            'Content': message
            }

        req = requests.post(self._webhook, data=json.dumps(payload))
        if req.status_code == 200:
            return True
        else:
            raise ChimeException(req.status_code)
