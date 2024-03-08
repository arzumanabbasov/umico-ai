import requests
from bs4 import BeautifulSoup
import json

with open('urls.txt', 'r') as f:
    urls = f.readlines()

# Initialize an empty dictionary to store data
data_dict = {}

def get_data(product_url):
    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    features_table = soup.find('div', class_='Features-Table-Once')

    rows = features_table.find_all('tr')

    extracted_data = {}

    for row in rows:
        columns = row.find_all('td')

        if len(columns) == 2:
            key = columns[0].text.strip()
            value = columns[1].text.strip()
            extracted_data[key] = value

    return extracted_data

for url in urls:
    data = get_data(url.strip())

    # Update the data_dict with the new data
    data_dict[url.strip()] = data
    break

# Write the data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file)

print("Data has been written to data.json")
