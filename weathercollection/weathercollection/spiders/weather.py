import scrapy
from weathercollection.items import WeathercollectionItem


class WeathercollectionSpider (scrapy.Spider):

    """Docstring for WeathercollectionSpider . """
    name = 'weather'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        item = WeathercollectionItem()
        item['city'] = response.xpath(
            '//*[@id="slider_ct_name"]/text()').extract()
        tenday = response.xpath('//*[@id="blk_fc_c0_scroll"]')
        item['date'] = response.css('p.wt_fc_c0_i_date::text').extract()
        item['daydesc'] = tenday.css('img.icons0_wt::attr(title)').extract()
        item['daytemp'] = tenday.css('p.wt_fc_c0_i_temp::text').extract()
        item['wind'] = tenday.css('p.wt_fc_c0_i_tip::text').extract()
        item['pm'] = tenday.css('li.l::text').extract()
        item['air'] = tenday.css('li.r::text').extract()
        return item
