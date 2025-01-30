import scrapy

class EventItem(scrapy.Item):
    title = scrapy.Field()       # Event title
    datetime = scrapy.Field()    # Event date and time
    location = scrapy.Field()    # Event location
    image_link = scrapy.Field()  # Link to event image