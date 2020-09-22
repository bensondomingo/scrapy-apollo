import scrapy
from scrapy.utils.response import open_in_browser
from urllib.parse import urljoin
from apollo.linkextractors import (
    CompanyDirectoryLinkExtractor, CompanyDetailLinkExtractor)


class CompanySpider(scrapy.Spider):
    name = 'companycrawler'
    base_url = 'appollo.io'
    allowed_domains = ['apollo.io']
    start_urls = ['https://www.apollo.io/directory/companies/A']

    def parse(self, response):
        # Go to the company directory list
        # For each item in directory list
        #   Go to item detail page
        #   Scrape item details
        company_dir = response.xpath(
            '//div[@class="h-100 p-3 DirectoryLetters__StyledCard-k1dfh4-3 fvykga card"]/ul/h3/text()').get()
        company_dir = company_dir.replace("'", '')
        company_dir_link_extractor = CompanyDirectoryLinkExtractor()
        dir_links = company_dir_link_extractor.extract_links(response)
        for link in dir_links:
            yield scrapy.Request(
                url=link.url,
                callback=self.company_directory_handler
            )

    def company_directory_handler(self, response):
        """ Parse company detail link """
        company_detail_link_extractor = CompanyDetailLinkExtractor()
        company_links = company_detail_link_extractor.extract_links(response)
        for link in company_links:
            yield scrapy.Request(
                url=link.url,
                callback=self.company_detail_handler,
                cb_kwargs={'directory': response.url}
            )

    def company_detail_handler(self, response, directory=None):
        print(response.url)
