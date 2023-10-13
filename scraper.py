import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

from main import rgb_to_cielab

url = 'https://minecraft.fandom.com/wiki/Map_item_format'

page = requests.get(url)
soup = bs(page.text, 'lxml')

table = soup.findAll('table')[1]

headers = []
for i in table.find_all('th'):
    title = i.text.rstrip()
    headers.append(title)

data = pd.DataFrame(columns = headers)
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text.rstrip() for i in row_data]
    length = len(data)
    data.loc[length] = row

data.drop('Color', inplace=True, axis=1)
data.drop('Blocks', inplace=True, axis=1)
data.drop(data.index[0:1], inplace=True)
data.reset_index(inplace=True, drop=True)

data['ID'] = data['ID'].apply(lambda x: x[2:].lstrip())
data['RGB'] = data['RGB'].apply(lambda x: x.replace(' ','').split(','))

data['RGB_Light'] = data['RGB'].apply(lambda x: [int(x) for x in x])
data['RGB_Normal'] = data['RGB_Light'].apply(lambda x: [x*220//255 for x in x])
data['RGB_Dark'] = data['RGB_Light'].apply(lambda x: [x*180//255 for x in x])

data['LAB_Light'] = data['RGB_Light'].apply(rgb_to_cielab)
data['LAB_Normal'] = data['RGB_Normal'].apply(rgb_to_cielab)
data['LAB_Dark'] = data['RGB_Dark'].apply(rgb_to_cielab)

data.drop('RGB', inplace=True, axis=1)
data.drop('RGB_Light', inplace=True, axis=1)
data.drop('RGB_Normal', inplace=True, axis=1)
data.drop('RGB_Dark', inplace=True, axis=1)

data.to_csv('mc_colors', index=False)
print(data)