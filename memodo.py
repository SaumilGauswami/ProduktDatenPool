import requests
from lxml import html
import pymysql
import config as db


class Memodo:

    def __init__(self):

        self.my_db = pymysql.connect(
            host=db.host,
            user=db.user,
            password=db.password,
            charset='utf8mb4'
        )
        self.my_cursor = self.my_db.cursor()

        self.get_urls()

    def get_urls(self):
        response = requests.get('https://www.memodo.de/')
        element = html.fromstring(response.text)

        urls = element.xpath('//li[@class="menu--list-item item--level-0 is--filter"]/a/@href')
        final = []
        for url in urls:
            page = 1
            while True:
                url_response = requests.get(url + f'?p={page}')

                if url_response.status_code == 200:
                    url_element = html.fromstring(url_response.text)
                    product_lists = url_element.xpath('//div[@class="product--info"]/a/@href')
                    if not product_lists:
                        break
                    for product in product_lists:
                        print(product)
                        final.append(product)
                        # self.get_details(product)
                    page += 1

                else:
                    break
        final = [*set(final)]
        print(len(final))

    def get_details(self, url):

        response = requests.get(url)
        element = html.fromstring(response.text)

        try:
            title = ''.join(element.xpath('//h1[@class="product--title"]//text()')).replace("\n", "").replace("\t",
                                                                                                              "").replace(
                "\r", "").replace("\a", "").strip()
        except:
            title = ''

        try:
            manufacturer_number = ''.join(element.xpath(
                '//li[@class="base-info--entry entry--manufacturer-sku"]/span[@class="entry--content"]//text()')).replace(
                "\n", "").replace("\t", "").replace("\r", "").replace("\a", "").strip()
        except:
            manufacturer_number = ''

        try:
            item_no = ''.join(element.xpath(
                '//li[@class="base-info--entry entry--sku"]/span[@class="entry--content"]//text()')).replace("\n",
                                                                                                             "").replace(
                "\t", "").replace("\r", "").replace("\a", "").strip()
        except:
            item_no = ''

        try:
            img = ''.join(element.xpath(
                '//li[@class="base-info--entry entry--sku"]/span[@class="entry--content"]//text()')).replace("\n",
                                                                                                             "").replace(
                "\t", "").replace("\r", "").replace("\a", "").strip()
        except:
            img = ''

        try:
            breadcrumb = '>'.join(
                element.xpath('//ul[@class="breadcrumb--list"]//span[@class="breadcrumb--title"]//text()')).replace(
                "\n", "").replace("\t", "").replace("\r", "").replace("\a", "").strip()
        except:
            breadcrumb = ''

        try:
            description = ''.join(
                element.xpath('(//div[@class="tab--container-list"])[1]//div[@class="tab--content"]//text()')).replace(
                "\n", "").replace("\t", "").replace("\r", "").replace("\a", "").strip()
        except:
            description = ''

        insert_query = f"""INSERT INTO {db.db_name}.{db.db_table_name} (link, manufacturer_no, articleNumber, title, breadcrums, description, image, sitename) VALUES ('{url}', '{manufacturer_number}', '{item_no}', '{title}', '{breadcrumb}', '{description}', '{img}', 'memodo');"""
        try:
            self.my_cursor.execute(insert_query)
            self.my_db.commit()
        except Exception as e:
            print(e)

        print(url)


if __name__ == '__main__':
    Memodo()
