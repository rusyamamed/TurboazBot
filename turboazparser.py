import os.path
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import datetime, time
current_directory = os.getcwd()

images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
#
class TurboAz:
    host = 'https://ru.turbo.az'
    url = 'https://ru.turbo.az/autos'
    lastkey = ""
    lastkey_file = ""
    today = datetime.date.today()
    todaydate = today.strftime("%d.%m.%Y")

    def __init__(self, lastkey_file):
        self.lastkey_file = lastkey_file

        if(os.path.exists(lastkey_file)):
            self.lastkey = open(lastkey_file, 'r').read()
        else:
            f = open(lastkey_file, 'w')
            self.lastkey = self.get_date()
            f.write(self.lastkey)
            f.close()

    def new_car(self):
        r = requests.get(self.url)
        print(r)
        html = BS(r.content, 'html.parser')
        new = []
        items = html.find_all('div', {'class':'products'})
        items = items[2].select('.products-i')
        print(items)
    
        for i in items:
            pubdate = self.get_lastdate(i)
#             link = self.parse_href(i)
#             carinfo = self.car_info(i)
#             print(carinfo)
                
            if(self.lastkey < pubdate):
                new.append(i)
        return new

    def car_info(self, uri):
        result = uri.select('.products-i__link')[0]['href']
        link = self.host + result
        r = requests.get(link)
        html = BS(r.content, 'html.parser')
 
        # parse poster image url
        image =  html.select('.product-photos > .product-photos-large')[0]['href']
        price =  html.select('.product-price')[0]
        title =  html.select('.product-name')[0]
 
        # form data
        info = {
            "date": self.get_lastdate(uri),
            "price": price.text,
            "title": title.text,
            "link": link,
            "image": image,
        };
        return info
 
    def download_image(self, url):
        r = requests.get(url, allow_redirects=True)
        a = urlparse(url)
        filename = os.path.basename(a.path)
        fullpath = f'{current_directory}/{images_folder}/{filename}'
#         basename = os.path.basename(fullpath)
#         print(filename)
#         print(os.path.basename)
        open(fullpath, 'wb').write(r.content)
        return fullpath
    
    def get_lastdate(self, date):
        items = date.select('.products-i__bottom > .products-i__datetime')
        datesplit = items[0].text.split(",")[1].lstrip()
        daystring = datetime.datetime.now().strftime("%d.%m.%Y")
        #hourdate = daystring + ' ' + datesplit.split()[1].lstrip()
        hourdate = self.todaydate + ' ' + datesplit.split()[1].lstrip()
        #datesplit = items[0].text.split(",")[1].lstrip()
        #datesplit = items[0].text.split(",")[1].lstrip()+items[0].text.split(",")[2]
        print(datesplit)
        datetypeformat = datetime.datetime.strptime(hourdate, '%d.%m.%Y %H:%M')
        date = time.mktime(datetypeformat.timetuple())
        #date = datetime.datetime.strptime(datesplit, '%d.%m.%Y')
        return str(date)
    def get_date(self, date):
        r = requests.get(self.url)
        html = BS(r.content, 'html.parser')
        items = html.find_all('div', {'class':'products'})
        items = date.select('.products-i__bottom > .products-i__datetime')
        datesplit = items[0].text.split(",")[1].lstrip()
        daystring = datetime.datetime.now().strftime("%d.%m.%Y")
        #hourdate = daystring + ' ' + datesplit.split()[1].lstrip()
        hourdate = self.todaydate + ' ' + datesplit.split()[1].lstrip()
        #datesplit = items[0].text.split(",")[1].lstrip()
        #datesplit = items[0].text.split(",")[1].lstrip()+items[0].text.split(",")[2]

        print(datesplit)
        datetypeformat = datetime.datetime.strptime(hourdate, '%d.%m.%Y %H:%M')
        date = time.mktime(datetypeformat.timetuple())
       # date = datetime.datetime.strptime(datesplit, '%d.%m.%Y')
        return str(date)
 
    def parse_href(self, href):
        result = href.select('.products-i__link')[0]['href']
        return result
 
    def update_lastdate(self, new_key):
        self.lastkey = new_key
 
        with open(self.lastkey_file, "r+") as f:
#             data = f.read()
            f.seek(0)
            f.write(str(new_key))
            f.truncate()
        return new_key


