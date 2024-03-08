import requests
from bs4 import BeautifulSoup
import requests


def collectUrls(maxUrls=1481):
    baseurl = 'https://umico.az'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/115.0.0.0 Safari/537.36'}

    with open('urls.txt', 'w') as file:
        for x in range(1, maxUrls + 1):
            url = f'https://umico.az/categories/3003-geyim-ve-ayaqqabi?page={x}'

            try:
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    product_list = soup.find_all('div', class_='MPProductItem')

                    for item in product_list:
                        for link in item.find_all('a', href=True):
                            url = baseurl + link['href']
                            file.write(url + '\n')
                else:
                    print("Wrong status code:", r.status_code)

            except requests.exceptions.RequestException as e:
                print('An error occurred:', e)


if __name__ == '__main__':
    collectUrls()
