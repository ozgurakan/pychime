# pyChime

pyChime makes it easy to post messages to Amazon Chime Chat Rooms using the Webhook.

## Sample Usage

At the moment Chime support sending messages.

```
from pychime import Chime, ChimeException

content = 'Hello World"
webhook = "https://hooks.chime.aws/incomingwebhooks/" \
        + "some_webhook_id_here" \
        + "?token=some_token_here",

chime = Chime(webhook)

try:
    chime.post(content)
except ChimeException as err:
    print('Error Code: {}, Error Message: {}'.format(err.code, err.message))

```