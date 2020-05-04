import json
import requests

class json_test(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        self.error = 0

    def json_check(self,cust_id):
        '''json_check: Compares the JSON response keys with the template stored , takes customer id as argument while
        object initialisation'''
        custid = {'csId':cust_id}
        result = requests.get("http://rheinau.lhs-systems.com:29003/rest/CIL/6/CUSTOMER.READ", auth=('AUT','AUT'), params=custid)
        #JSON response is stored in resp dictionary
        resp = result.json()
        f = open('responsi.txt', 'wb')
        f.write('dict = ' + repr(resp) + '\n')
        f.close()

        #JSON template is stored as in a separate file : json_template
        with open("./to_checkin/json_template",'r') as jfile:
            json_temp= jfile.read()

        parsed_json = json.loads(json_temp)

        diff_list=[key for key in resp.keys() if key not in parsed_json]

        if diff_list:
            print "\nError : Response JSON structure is NOT matching, check the actual response !!"
            print "\nTotal keys not matched: {0}\n".format(len(diff_list))
            print " , ".join(diff_list)
            raise Exception("Json Check Failed !!")
        else:
            print "\nThe JSON structure is matching with the template!"

ob = json_test()
ob.json_check(29)

