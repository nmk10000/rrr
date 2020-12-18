from datetime import timedelta, datetime
from dateutil import parser
from pprint import pprint
from time import sleep
import requests
import feedparser

BOT_TOKEN = '1050654922:AAGqSBiECbkUr8RT57MrQAwk7i4iOCBvCBo'
CHANNEL_ID = '@aaafsdgy' # @bot_channel_name
FEED_URL = 'https://ekitten.co/?action=display&bridge=Instagram&context=Hashtag&h=mallutrolls&media_type=picture&format=Atom' # https://something.com/feeds/rss.xml


def send_message(message):
    requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}')


def main():
    rss_feed = feedparser.parse(FEED_URL)

    for entry in rss_feed.entries:

        parsed_date = parser.parse(entry.published)
        parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None) # remove timezone offset
        now_date = datetime.utcnow()

        published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
        if published_20_minutes_ago:
            send_message(entry.links[0].href)
            print(entry.links[0].href)


if __name__ == "__main__":
    while(True):
        main()
        sleep(10 * 30)
