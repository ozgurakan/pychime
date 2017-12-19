# pyChime

pyChime makes it easy to post messages to Amazon Chime Chat Rooms using the Webhook.

## Sample Usage

At the moment Chime supports sending messages.

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
## More Complex Example with rssfeeder

```
from pychime import Chime, ChimeException
from rssfeeder import Feeder, Poster

class MyPoster(Poster):
    """
    Posts the feed to the Chime Chat Room
    """
    def __init__(self, webhook):
        self._webhook = webhook
        super().__init__()

    def post(self, feed):
        """ Post the feed to Chime Chat Room """
        print('Posting {} to chime'.format(feed.id))
        chime = Chime(self._webhook)

        content = ''
        content += feed.title + '\n\n'
        content += feed.published + '\n\n'
        content += feed.summary + '\n\n'
        content += feed.link + '\n\n'

        if len(feed.tags) > 0:
            content += 'category: ' + feed.tags[0]['term'] + '\n'

        try:
            chime.post(content)
        except ChimeException as err:
            print('Error Code: {}, Error Message: {}'.format(err.code, err.message))
            return False
        return True

if __name__ == "__main__":
    dynamodb_table = "chimetest1"
    rss_feed_url = "http://feeds.feedburner.com/amazon/newsblog"
    chime_web_hook = "https://hooks.chime.aws/incomingwebhooks/some_chime_webhook_id?token=some_token_here"

    tochime = MyPoster(chime_web_hook)
    feeder = Feeder(rss_feed_url, dynamodb_table, tochime)
    feeder.process_feeds()
```