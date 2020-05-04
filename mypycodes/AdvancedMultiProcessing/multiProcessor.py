import requests
import multiProcessor

def response_timer(uri,ip_param=""):
    r = requests.session()
    headers = {'content-type': 'application/json'}
    r.auth = ('AUT','AUT')
    r.headers.update(headers)
    resp = r.get(uri,params=ip_param)

if __name__ == '__main__':
    out = []
    for i in range(3):
        p = multiProcessor.Process(target=response_timer(), args=('http://rheinau.lhs-systems.com:29001/dil/rest/CIL/6/CURRENCIES.READ',))
        out.append(p)
        p.start()