import config as db
import requests
import gzip
from io import BytesIO
import re
from lxml import html
import pymysql


conection = pymysql.connect(host=db.host, user=db.user, password=db.password, charset='utf8mb4')
cursor = conection.cursor()


def get_url():
    sitemap_url = 'https://shop.krannich-solar.com/de-en/sitemap_index.xml'
    sitemap_response = requests.get(sitemap_url).text
    all_gz_url = re.findall('<loc>(.*?)</loc>', str(sitemap_response))
    for url in all_gz_url:
        response = requests.get(url)

        if response.status_code == 200:
            content = gzip.GzipFile(fileobj=BytesIO(response.content)).read()
            all_links = re.findall('<loc>(.*?)</loc>', str(content))
        else:
            print("Failed to fetch the .xml.gz file")
            all_links = None

        for link in all_links:
            get_details(link)


def get_details(link):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(
        link,
        headers=headers,
    )
    dom = html.fromstring(response.text)

    try:
        article_number = "".join(dom.xpath('//div[@class="product--ordernumber"]/text()')).replace("'", "`").strip()
    except:
        article_number = None
    try:
        product_name = "".join(dom.xpath('//h1[@class="product--title"]/text()')).replace('\n','').replace("'", "`").strip()
    except:
        product_name = None

    try:
        product_image="".join(dom.xpath('//img[@itemprop="image"]/@src'))
    except:
        product_image=None

    try:
        product_image = ", ".join(product_image) if len(product_image) > 1 else product_image
    except:
        product_image = None
    try:
        bread_crums=" > ".join(dom.xpath('//span[@class="breadcrumb--title"]/text()')).replace('\n','').replace(' ','').replace("'", "`").strip()
    except:
        bread_crums=None

    description = dict()
    description['PRODUCT INFORMATION'] = ",".join(dom.xpath('//div[@class="product--description--wrapper"]/div/text()')).replace('\n','').replace("'", "`").strip()
    if not description['PRODUCT INFORMATION']:
        description['PRODUCT INFORMATION']="".join(dom.xpath('//div[@itemprop="description"]/div/text()')).replace('\n','').replace("'", "`").strip()
    technical_details = {}
    try:
        technical_table = dom.xpath('//div[@data-tab-id="technical_data"]//tr[@class="product--properties-row"]')
    except:
        technical_table=None
    technical_data = {}

    for t in technical_table:
        tech = {}
        key = "".join(t.xpath('./td[1]/text()')).replace(':','').replace("'", "`")
        value = "".join(t.xpath('./td[2]/text()')).replace(':', '').replace("'", "`")
        tech[key] = value
        technical_data.update(tech)
    technical_details['TECHANICAL DATA'] = technical_data

    article_detail = dict()
    try:
        article_details = dom.xpath('//div[@data-tab-id="ArticleDetails"]//tr[@class="product--properties-row"]')
    except:
        article_details=None
    for a in article_details:
        art = {}
        key = "".join(a.xpath('./td[1]/text()')).replace(':','').replace("'", "`")
        value = "".join(a.xpath('./td[2]/text()')).replace(':', '').replace("'", "`")
        art[key] = value
        article_detail.update(art)
    technical_details['ARTICLES DETAILS'] = article_detail

    packaging = dict()
    try:
        packaging_details = dom.xpath('//div[@data-tab-id="Packaging"]//tr[@class="product--properties-row"]')
    except:
        packaging_details=None
    for p in packaging_details:
        pac = {}
        key = "".join(p.xpath('./td[1]/text()')).replace(':','').replace("'", "`")
        value = "".join(p.xpath('./td[2]/text()')).replace(':', '').replace("'", "`")
        pac[key] = value
        packaging.update(pac)
    technical_details['PACKAGING DETAILS'] = packaging

    dimensions = dict()
    dimensions_details = dom.xpath('//div[@data-tab-id="dimensions"]//tr[@class="product--properties-row"]')
    for d in dimensions_details:
        dimension = {}
        key = "".join(d.xpath('./td[1]/text()')).replace(':','').replace("'", "`")
        value = "".join(d.xpath('./td[2]/text()')).replace(':', '').replace("'", "`")
        dimension[key] = value
        dimensions.update(dimension)
    technical_details['DIMENSIONS'] = dimensions

    Warranty = dict()
    Warranty_details = dom.xpath('//div[@data-tab-id="Warranty"]//tr[@class="product--properties-row"]')
    for W in Warranty_details:
        war = {}
        key = "".join(W.xpath('./td[1]/text()')).replace(':','').replace("'", "`")
        value = "".join(W.xpath('./td[2]/text()')).replace(':', '').replace("'", "`")
        war[key] = value
        Warranty.update(war)
    technical_details['WARRANTY'] = Warranty

    description['Technical details'] = technical_details

    insert_query = f"""INSERT INTO {db.db_name}.{db.db_table_name} (link, manufacturer_no, articleNumber, title, breadcrums, description, image, sitename) VALUES ('{link}', '', '{article_number}', '{product_name}', '{bread_crums}', '{description}', '{product_image}', 'krannich');"""
    try:
        cursor.execute(insert_query)
        conection.commit()
    except Exception as e:
        print(e)


get_url()
