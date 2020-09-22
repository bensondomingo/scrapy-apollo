# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
from itemloaders.processors import MapCompose, Join
import scrapy
from dataclasses import dataclass
from scrapy.loader import processors


class CompanyItem(scrapy.Item):
    name = scrapy.Field(default='NA')
    industry = scrapy.Field(default='NA')  # rename to industry
    logo = scrapy.Field(default='NA')
    website = scrapy.Field(default='NA')
    phone = scrapy.Field(default='NA')
    employees = scrapy.Field(default='NA')
    headquarters = scrapy.Field(default='NA')
    tags = scrapy.Field(default='NA')
    about = scrapy.Field(default='NA')
    directory = scrapy.Field(default='NA')
