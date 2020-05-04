# Keywords to parse the input data into a JSON string without sorting any attributes.
# <used to serialize input data for REST requests>
import json
from collections import OrderedDict

def parse_data(data=None):
    """Converts input data into ordered dictionary
    and returns a valid JSON formatted string if data is passed, else returns empty JSON string.
    :param data: <input data to be sent along with the REST request(can be empty)>
    """
    restdata = json.loads(data ,object_pairs_hook=OrderedDict) if data else {}
    return json.dumps(restdata)

def parse_data_file(data_file=None):
    """Consumes a file, converts it into ordered dictionary
    and returns a valid JSON formatted string if data file is passed, else returns empty JSON string.
    :param data: <input data file name to be sent along with the REST request(can be empty)>
    """
    with open(data_file, 'r') as json_file:
        restdata = json.load(json_file ,object_pairs_hook=OrderedDict) if data_file else {}
    return json.dumps(restdata)
