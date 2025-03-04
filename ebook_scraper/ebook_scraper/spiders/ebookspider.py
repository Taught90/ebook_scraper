
import scrapy

class EbookspiderSpider(scrapy.Spider):
    name = "ebookspider"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        
        book_urls = response.css('h3 a::attr(href)').getall()
        for book_url in book_urls:
            full_url = response.urljoin(book_url)  # Convert relative URL to absolute
            yield scrapy.Request(url=full_url, callback=self.parse_details)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)

    def parse_details(self, response):
        yield{
            'title': response.css('div.product_main h1::text').get(),
            'instock availability': response.css('p.instock').get().strip().replace('<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        ', '').replace('\n    \n</p>', ''),
            'UPC': response.css('tr:nth-child(1) td::text').get(),
            'product type': response.css('tr:nth-child(2) td::text').get(),
            'price excluding tax': response.css('tr:nth-child(3) td::text').get().replace('£', '').strip(),
            'price incuding tax': response.css('tr:nth-child(4) td::text').get().replace('£', '').strip(),
            'tax': response.css('tr:nth-child(5) td::text').get().replace('£', '').strip(),
            'number of reviews': response.css('tr:nth-child(7) td::text').get(),
            }