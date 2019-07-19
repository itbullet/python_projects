import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        links = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open("link.log", "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url and "http" in url:
                    print("\n" + url)
                    f.write("%s\n" % url)

news = "https://www.rambler.ru/"
Scraper(news).scrape()