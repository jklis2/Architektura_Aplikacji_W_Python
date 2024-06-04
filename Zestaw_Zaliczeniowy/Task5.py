import requests
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/cd_catalog.xml"

response = requests.get(url)
xml_data = response.content

root = ET.fromstring(xml_data)

cd_list = []
for cd in root.findall('CD'):
    artist = cd.find('ARTIST').text
    title = cd.find('TITLE').text
    cd_list.append((artist, title))

print(cd_list)
