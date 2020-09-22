from scrapy.loader import ItemLoader
from scrapy.loader import processors

from apollo.items import CompanyItem


class CompanyItemLoader(ItemLoader):
    default_item_class = CompanyItem
    default_output_processor = processors.TakeFirst()

    def __init__(self, response, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = response
        self.selector = response.xpath('//div[@class="ProfileCard__StyledInnerContainer-sc-18kiizh-1 jwzMjl"]/div/div')

    def populate_item_fields(self):
        self.add_xpath('name', '//div[@class="CompanyCard__CompanyName-sc-1nf6h6-4 jjZZR"]/text()')
        self.add_xpath('industry', '//div[@class="mb-2 text-capitalize CompanyCard__CompanyIndustry-sc-1nf6h6-6 caUrdc"]/text()')
        self.add_xpath('logo', '//img[@alt="Logo"]/@src')
        self.add_xpath('website', '//a[@class="UnStyledA-dvuh11-0 bFxflP"]/@href')
        self.add_xpath('phone', '//div[@style="color:#1b1441;font-weight:900"]/text()', re=r'^.+\d{3,}$')
        # self.add_xpath('employees', '//div[@style="color:#1b1441;font-weight:900"]/text()', re=r'\d{1,}')
        self.add_value('employees', self._get_employees())
        self.add_xpath('headquarters', '//div[@style="color:#1b1441;font-weight:900"]/div[@class="text-capitalize"]/text()')
        self.add_xpath('tags', '//div[@class="CompanyCard__PaddedCol-sc-1nf6h6-0 eTSRJP col-12"]/div/div[@style="color:#1b1441;font-weight:900"]/text()')
        self.add_xpath('about', '//div[@class="collapse ExpandableSection__ScrollableContainer-rkezx2-1 hOutNu"]/text()')
    
    def _get_employees(self):
        emp = 'NA'
        for c in self.response.xpath('//div[@style="display:flex;flex-direction:column"]'):
            key = c.xpath('div[@style="color:#7a7e8b"]/text()').get().lower()
            if key == 'employees':
                emp = c.xpath('div[@style="color:#1b1441;font-weight:900"]/text()').get()
                break
        return emp
