import scrapy

class JobSpider(scrapy.Spider):
    name = 'jobspider'
    start_urls = ['https://www.indeed.com/jobs?q=Python&l=Coppell,+TX&explvl=entry_level']

    def parse(self, response):
        for title in response.css('#resultsCol > div.result > h2 > a'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('#resultsCol > div.pagination > a'):
            yield response.follow(next_page, self.parse)
