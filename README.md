# E-BOOK SCRAPER
- This is an e-book online scraper using the scrapy framework. The link to the website is http://books.toscrape.com/.
## CREATING THE PROJECT
- To open your new project:
  - Open a directory in you code editor.
  - type 'scrapy startproject ebook_scraper'.
  - Then 'cd ebook_scraper' to enter the new directory.
## CREATING A SPIDER
- We now need a spider to help in crawling, to create it we:
  - type 'scrapy genspider ebookspider http://books.toscrape.com/'.
- Open the ebookspider.py file in the spider folder.
## CRAWLING USING THE SPIDER
- To crawl type 'scrapy crawl ebookspider'
- To save the data in a json format type 'scrapy crawl ebookspider -O filename.json'
- To save the data in a csv format type 'scrapy crawl ebookspider -O filename.csv'
