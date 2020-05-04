#######################################################################################################################
# This Library verifies the REST response.
# This is required to isolate the REST response value verification from other rest services keywords
# and to provide a generic stand alone approach on JSON verification and validation.
#
# TODO#
#
#
#
# __author__ = "empqtut"
# __version__ = "1.0.dev1"
# __email__ = "manikandan.chandrasekaran@ericsson.com"
# __status__ = "Development"
#######################################################################################################################


import _utils
import mapper

class ResponseVerifier:
    """
    Verifies the key-value pairs of the response JSON with expected json
    """

    def __init__(self):
        self.rc_mapper = mapper.Mapper()

    def serialize_json(self, input_json):
        """
        function to serialize the nested lists and dictionaries of the input JSON
        and return a simple flat dictionary.
        :param input_json:
        :return:
        """
        list_parsed_json = _utils.parse_list(input_json)
        flat_json = _utils.parse_dict(list_parsed_json)
        return flat_json

    def json_value_checker(self, actual_json, sid_reference, schme_url,**kwargs):
        """
        verifies if key/value pair from actual json is present in expected json.
        raises different exception for various mismatch
        :param actual_json:
        :param expected_json:
        :return:
        """
        actual_json_flat = _utils.atomize_dict(actual_json)
        expected_json_flat = self.rc_mapper.json_mapper(sid_reference, schme_url, **kwargs)
        matched_keys = []
        for k, v in actual_json_flat.iteritems():
            if k not in expected_json_flat.keys():
                raise Exception("Key {0} not found in expected json".format(k))
            elif v not in expected_json_flat.values():
                raise Exception("Value {0} not found in expected json".format(v, k))
            elif actual_json_flat[k] != expected_json_flat[k]:
                raise Exception("Value {0} for key {1} not found in expected json".format(actual_json_flat[k], k))
            else:
                matched_keys.append(k)
        return "Items in actual json present in expected json\nKeys verified :\n{0}".format(matched_keys)

class_handle = ResponseVerifier()
actual_j = _utils.read_json_data('../JsonSamples/actual.json')
uri = "http://rome.lhs-systems.com:29001/dil/rest/jsonschema/customerContactGet/response/v1"
print class_handle.json_value_checker(actual_j,'contactRole',uri,**{"customer_id": "12", "CCBILL": 'X'})