import requests
from bs4 import BeautifulSoup
import csv

def main(url):
    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = [item.text for item in soup.select("loc")]
        with open("data.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Url", "Status Code"])
            for link in links:
                r = req.get(link)
                print(link, r.status_code)
                writer.writerow([link, r.status_code])
                soup = BeautifulSoup(r.content, 'html.parser')
                end = [item.text for item in soup.select("loc")]
                for a in end:
                    r = req.head(a)
                    print(a, r.status_code)
                    writer.writerow([a, r.status_code])

main("https://www.nemora.it/sitemap_index.xml")