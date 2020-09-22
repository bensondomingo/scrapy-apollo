from scrapy.linkextractors import LinkExtractor
from scrapy.utils.python import unique


class CompanyDirectoryLinkExtractor(LinkExtractor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow = r'/directory/companies/[A-Z]/\d{1,}'
        self.restrict_xpaths = (
            '//div[@class="h-100 p-3 DirectoryLetters__StyledCard-k1dfh4-3 fvykga card"]/ul/li',)
        self.unique = True
        self.strip = True


class CompanyDetailLinkExtractor(LinkExtractor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow = r'^/companies/.*/.*'
        self.restrict_xpaths = (
            '//div[@class="h-100 p-3 DirectoryLetters__StyledCard-k1dfh4-3 fvykga card"]/ul/li/a[@class="UnStyledA-dvuh11-0 bFxflP"]',)
        self.unique = True
        self.strip = True
