# ####################################################################################################################
# utilities
# __author__ = "empqtut"
# __version__ = "1.0.dev1"
# __email__ = "manikandan.chandrasekaran@ericsson.com"
# __status__ = "Development"
#######################################################################################################################
import json
import jsonref


from urlparse import (urlparse,urljoin, urlunsplit, SplitResult, urlsplit as _urlsplit)

def read_json_schema_from_file(filename):
    """ reads a json file and returns a python dictionary """
    with open(filename, 'r') as raw_file:
        json_temp = raw_file.read()
    return jsonref.loads(json_temp.decode("utf-8"))

def read_json_schema_from_url(url):
    """ reads a json file from url and returns a python dictionary without reference"""
    return jsonref.load_uri(url)

def read_json_data(filename):
    """ reads a json file and returns a python dictionary   """
    with open(filename, 'r') as raw_file:
        json_temp = raw_file.read()
    return json.loads(json_temp.decode("utf-8"))

def read_json_url(uri):
    """ reads json schema from url"""
    json_schema_temp = uri.getdata()
    return json.loads(json_schema_temp.decode("utf-8"))


def json_combiner(*args):
    """combines multiple jsons into a single json and returns a py dict"""
    combined_json = {}
    for di in args:
        combined_json.update(di)
    return combined_json


def urlsplit(url):
    parsed_url = urlparse(url)
    print parsed_url
    # if "#" in path:
    #     path, fragment = path.split("#", 1)
    # return SplitResult(scheme, netloc, path, query, fragment)


def json_prop_finder(json_schema):
    """reads properties key from JSON schema"""
    if 'properties' in json_schema:
        return json_schema['properties']
    else:
        raise Exception("Properties not found in JSON schema")

def expected_json_creator(expected_soi, ref):
    """creates expected json from the JSON Reference and the schema"""
    expected_final = {}
    for key, value in ref.iteritems():
        if key in expected_soi:
            expected_final[value] = expected_soi[key]
    return expected_final

def getByDotNotation(obj,ref):
    val = obj
    for key in ref.split('.'):
       val = val[key]
    return val


def atomize_dict(ip_dict, dict_key = None,dict_val = None):
    res = {}
    def recurse(input_dict):
        for k,v in input_dict.iteritems():
            if isinstance(v,dict):
                recurse(v)
            else:
                res[k]= v
    recurse(ip_dict)
    if dict_key or dict_val:
        for ky,val in res.items():
            if ky == dict_key:
                return val
            elif val == dict_val:
                return ky
    else:
        return res


def parse_dict(input_json):
    """
    gets any dictionary as input and returns a flattened dictionary
    :param input_json:
    :return:
    """

    def _child_finder(key, value):
        """
        internal function to iterate over the dictionary and flatten the dict with . operator
        :param key:
        :param value:
        :return:
        """
        if isinstance(value, dict):
            return [(key + '.' + k_child, v_child) for k_child, v_child in parse_dict(value).items()]
        else:
            return [(key, value)]

    result_list = [item for ky, val in input_json.items() for item in _child_finder(ky, val)]
    return dict(result_list)


def parse_list(input_json):
    """
    detects any list inside input json and flattens itself and any dictionaries inside it
    :param input_json:
    :return:
    """
    temp_val_holder = {}
    for key, value in input_json.items():
        if isinstance(value, list):
            for val in value: pass
        #         temp_result_dic.update(val)
        #     temp_result_dic[key] = temp_val_holder
        #
        # return parse_dict(temp_result_dic)