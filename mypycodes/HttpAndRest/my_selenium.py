# ####################################################################################################################
# simple customised keywords for html and web scrapping operations using selenium library
#
# TODO : Can be enhanced with BeautifulSoup/Scrappy for more sophisticated GUI testing keywords
#
# __author__ = "empqtut"
# __version__ = "1.0.dev1"
# __email__ = "manikandan.chandrasekaran@ericsson.com"
# ###################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://rome.lhs-systems.com:29001/custcare_cu/")

elems = driver.find_elements_by_xpath("//a[@href]")
driver.close()
driverCE.findElement(By.xpath("//div[@id='testId']/a")).getAttribute("href");