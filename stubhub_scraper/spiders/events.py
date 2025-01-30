import scrapy
import json
import re
from stubhub_scraper.items import EventItem


class StubHubEventSpider(scrapy.Spider):
    name = 'events'

    start_urls = [
        'https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&page=0&tlcId=2'
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 5  # This sets the delay between requests to 2 seconds
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for event in data['events']:
            item = EventItem()
            item['title'] = event['name']
            item['datetime'] = event['formattedDateWithoutYear'] + ' ' + event['formattedTime']
            item['location'] = event['venueName'] + ' ' + event['formattedVenueLocation']
            item['image_link'] = event['imageUrl']
            yield item


        current_page_match = re.search(r'page=(\d+)', response.url)

        if current_page_match:
            current_page = int(current_page_match.group(1))
        else:
            current_page = 0

        next_page = current_page + 1

        # Construct the next page URL by updating the 'page' parameter using regex
        next_page_url = re.sub(r'page=\d+', f'page={next_page}', response.url)

        # If additional pages with events are available, send a request to retrieve the next page
        if len(data['events']) > 0:  # Verify whether the current page contains any event listings
            yield scrapy.Request(next_page_url, callback=self.parse)