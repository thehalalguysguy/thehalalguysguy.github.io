import io
import re
import json
from bs4 import BeautifulSoup
from zipfile import ZipFile

with io.open('gpt/Halal Trucks NYC.kmz', 'rb') as f:
  kmz = ZipFile(f)
  kml = kmz.open('doc.kml', 'r').read()
  soup = BeautifulSoup(kml, 'xml')
  print(soup.prettify())
  # split by <name> tag
  names = soup.find_all('name')
  for name in names:
    # find coordinates
    if name.find_next_sibling('Point'):
      coords = name.find_next_sibling('Point').find('coordinates').text
      print(name.text.strip())
      if coords:
        # split coordinates by comma
        coords = coords.strip().split(',')
        # print longitude and latitude
        print(' ', coords[0], coords[1])
        lat = coords[1]
        lon = coords[0]
    # find all img tags
    desc = name.find_next_sibling('description')
    if desc:
      # find all text between 'img src=" and "'
      imgs = re.findall(r'img src="([^"]+)"', desc.text)
      for img in imgs:
        print(' ', img)
    print('\n')