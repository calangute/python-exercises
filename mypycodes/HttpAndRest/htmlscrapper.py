# ####################################################################################################################
# simple keywords for html and web scrapping operations
#
# TODO : Should be enhanced with BeautifulSoup/Scrappy for more sophisticated GUI testing keywords
#
# __author__ = "empqtut"
# __version__ = "1.0.dev1"
# __email__ = "manikandan.chandrasekaran@ericsson.com"
# #####################################################################################################################

from lxml import html
import requests


def extract_href(url):
    """extracts hrefs from a given url - uses lxml parser"""
    data = requests.get(url)
    html_struct = html.fromstring(data.content)
    return html_struct.xpath('//a/@href')

data = extract_href('http://ch-kumarran-7.lhs-systems.com:8082/cx/login')
result = [a for a in data if "005" in a]
print data




