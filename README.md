**Finding the Data Source:** First, I located the API that provides the event details and verified that the data matches what is displayed on the website.

**Sending Requests:** Scrapy was used to make API requests and fetch data efficiently.

**Avoiding Blocks:** To prevent being detected as a bot, I added a fake User-Agent to the middleware, making the requests appear more like real browser traffic.

**Respecting Server Limits:** To avoid overwhelming the website, a small delay of 5 seconds was added between requests using Scrapy’s DOWNLOAD_DELAY setting.

**Handling Pagination:** Since events were spread across multiple pages, I implemented logic to track page numbers and continue requesting additional pages until all data was collected.

**Saving the Data:** The extracted data was stored in a JSON file. The settings used were:

***FEED_FORMAT*** = 'json' -> Saves the output in JSON format.

***FEED_URI*** = 'events.json' -> Stores the data in a file named events.json.

Other formats like CSV or XML can also be used by adjusting FEED_FORMAT.
