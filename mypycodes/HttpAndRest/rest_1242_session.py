import requests


s = requests.session()

s.url = "http://rome.lhs-systems.com:29001"


print s.get('/dil/rest/v1/customer/BUS0000000000011/contact/contactRole/B')