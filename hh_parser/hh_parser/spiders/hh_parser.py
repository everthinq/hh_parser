import scrapy
from ..items import HhParserItem

from bs4 import BeautifulSoup as BS


class hh_parser(scrapy.Spider):
    name = 'hh_parser' # name of spider must be the same as filename
    start_urls = [
                    'https://usa.hh.ru/employers_company?area=113',
                    'https://usa.hh.ru/employers_company?area=5',
                    'https://usa.hh.ru/employers_company?area=40',
                    'https://usa.hh.ru/employers_company?area=9',
                    'https://usa.hh.ru/employers_company?area=16',
                    'https://usa.hh.ru/employers_company?area=28',
                    'https://usa.hh.ru/employers_company?area=48',
                    'https://usa.hh.ru/employers_company?area=97',
                    'https://usa.hh.ru/employers_company?area=1001'
                 ]


    def parse(self, response): # overrided parse method for recursive requests
        soup = BS(response.text, 'html.parser')
        companies = soup.find_all(class_ = 'employers-company__item')

        for i in range(0, len(companies)):
            url = companies[i]['href']
            url = url.split('?')[0] + '/page-0?' + url.split('?')[1]

            if not 'informacionnye_tekhnologii' in url:
                industry_name = companies[i].text
                full_url = response.urljoin(url)

                yield scrapy.Request(full_url,
                                     callback = self.parse_industry,
                                     meta = {'industry_name' : industry_name})


    def parse_industry(self, response):
        soup = BS(response.text, 'html.parser')
        companies = soup.findAll('div', class_ = 'employers-company__item')

        is_next_page = soup.find('a',
                                 class_ = 'b-pager__next-text m-active-arrow HH-Pager-Controls-Next HH-Pager-Control')

        if is_next_page:
            for each in companies:
                href = 'https://hh.ru/' + each.a['href']
                company_name = each.text[:-2]
                industry_name = response.meta['industry_name']

                page = int(response.url.split('?')[0].split('-')[1])
                page += 1

                url = response.url.split('?')[0].split('-')[0] + '-' + str(page) + '?' + response.url.split('?')[1]

                if url.split('?')[1].split('=')[1] == '113':
                    country = 'Russia'

                if url.split('?')[1].split('=')[1] == '5':
                    country = 'Ukraine'

                if url.split('?')[1].split('=')[1] == '40':
                    country = 'Kazakhstan'

                if url.split('?')[1].split('=')[1] == '9':
                    country = 'Azerbaijan'

                if url.split('?')[1].split('=')[1] == '16':
                    country = 'Belarus'

                if url.split('?')[1].split('=')[1] == '28':
                    country = 'Georgia'

                if url.split('?')[1].split('=')[1] == '48':
                    country = 'Kyrgyzstan'

                if url.split('?')[1].split('=')[1] == '97':
                    country = 'Uzbekistan'

                if url.split('?')[1].split('=')[1] == '1001':
                    country = 'Other countries'

                industry = industry_name
                company = company_name
                company_url = href

                item = HhParserItem()

                item['COUNTRY'] = country
                item['INDUSTRY'] = industry
                item['COMPANY'] = company
                item['COMPANY_URL'] = company_url

                yield item

                yield scrapy.Request(url,
                                 callback = self.parse_industry,
                                 meta = {'industry_name' : industry_name})

        if is_next_page == None:
            for each in companies:
                href = 'https://hh.ru/' + each.a['href']
                company_name = each.text[:-2]
                industry_name = response.meta['industry_name']

                page = int(response.url.split('?')[0].split('-')[1])
                page += 1

                url = response.url.split('?')[0].split('-')[0] + '-' + str(page) + '?' + response.url.split('?')[1]

                if url.split('?')[1].split('=')[1] == '113':
                    country = 'Russia'

                if url.split('?')[1].split('=')[1] == '5':
                    country = 'Ukraine'

                if url.split('?')[1].split('=')[1] == '40':
                    country = 'Kazakhstan'

                if url.split('?')[1].split('=')[1] == '9':
                    country = 'Azerbaijan'

                if url.split('?')[1].split('=')[1] == '16':
                    country = 'Belarus'

                if url.split('?')[1].split('=')[1] == '28':
                    country = 'Georgia'

                if url.split('?')[1].split('=')[1] == '48':
                    country = 'Kyrgyzstan'

                if url.split('?')[1].split('=')[1] == '97':
                    country = 'Uzbekistan'

                if url.split('?')[1].split('=')[1] == '1001':
                    country = 'Other countries'

                industry = industry_name
                company = company_name
                company_url = href

                item = HhParserItem()

                item['COUNTRY'] = country
                item['INDUSTRY'] = industry
                item['COMPANY'] = company
                item['COMPANY_URL'] = company_url

                yield item