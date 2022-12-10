import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    url = 'https://www.indeed.com/jobs?q=python+developer&l=New+York%2C+NY&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_ = 'heading4')
    for item in divs:
        title= item.find_next('a').text
        company = item.find_next('span', class_ = 'companyName').text
        try:
            salary = item.find('div', class_ = 'attribute_snippet').text.strip()
        except:
            salary = ''
        try:
            summary = item.find('div', class_ = 'job-snippet').text.strip()
        except:
            salary = ''

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary,
        }
        joblist.append(job)
    return

joblist = []
c = extract(0)
transform(c)
print(len(joblist))