import requests
import xml.etree.ElementTree as ET

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso/FullCountryInfoAllCountries"
response = requests.get(url)

if response.status_code == 200:
    root = ET.fromstring(response.content)
    countries_languages = {}

    for country_info in root.findall('tCountryInfo'):
        country_name = country_info.find('sName').text
        languages = []

        for language in country_info.findall('Languages/tLanguage'):
            language_name = language.find('sName').text
            languages.append(language_name)
    
        countries_languages[country_name] = languages
        