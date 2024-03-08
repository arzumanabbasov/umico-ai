import requests
from bs4 import BeautifulSoup

BASE_DIR = 'C:/Users/Admin/Desktop/umico-ai'


def download_and_save_image(product_url):
    response = requests.get(product_url)

    file_name = product_url.split('-')[0].split('/')[-1]

    soup = BeautifulSoup(response.content, 'html.parser')

    image_class = soup.find('div', class_='MPProductSlider-Main-Image')

    img_tag = image_class.find('img')

    # Extract the image URL
    image_url = img_tag['src'].replace('/_ipx/_/', '')
    print(image_url)

    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(BASE_DIR + f'/data/raw/img/{file_name}.png', 'wb') as f:
            f.write(response.content)
        print('Image downloaded successfully.')
    else:
        print(f'Failed to download image. Status code: {response.status_code}')


def write_last_url(url):
    with open('lasturl.txt', 'w') as last_url_file:
        last_url_file.write(url)


def download_all_images():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    count = 0

    for url in urls:
        download_and_save_image(url.strip())
        count += 1

        if count % 1000 == 0:
            write_last_url(url.strip())

    # If the total number of URLs is not a multiple of 1000, write the last URL
    if count % 1000 != 0:
        write_last_url(url.strip())


if __name__ == '__main__':
    download_all_images()
