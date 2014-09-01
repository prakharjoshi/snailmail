import scrapy
from damail.items import DamailItem

class damailSpider(scrapy.Spider):
	name = "damail"
	allowed_domains = ['hostel.daiict.ac.in']
	start_url = [
			"http://hostel.daiict.ac.in/index.php?option=com_eventtableedit&view=default&Itemid=2"
	]

	def parse(self, response):
		for sel in response.xpath('//tr[@class="linecolor1"]'):
			item = DamailItem()
			for i in range(1,500):
				a = i+1
				b = i+2
				item['name'] = sel.xpath('td[@class="evtda"]/text()').extract()
				item['room'] = sel.xpath('td[@class="evtdb"]/text()').extract()
				i = i+10
			yield item