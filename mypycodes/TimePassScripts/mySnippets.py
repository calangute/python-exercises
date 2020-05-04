def expected_json_creator(self, expected_soi, ref):
    """creates expected json from the JSON Reference and the schema"""
    expected_final = {}
    for key, value in ref.iteritems():
        if key in expected_soi:
            expected_final[value] = expected_soi[key]
    return expected_final


def json_data_creator(self, json_schema):
    json_properties = self._json_prop_finder(json_schema)

    def _keys_updater(di, val={}):
        return {key: val for key in di.keys()}

    def _prop_parser(json_prop):
        for key, value in _child_finder(json_prop):
            if key == "$ref":
                return value.split("/")

    def _child_finder(key, value):


class DotAccessibleDict ( object ):
  def __init__ ( self, data ):
    self._data = data

  def __getitem__ ( self, name ):
    val = self._data
    for key in name.split( '.' ):
      val = val[key]
    return val

def getByDotNotation(obj,ref):
  val = obj
  for key in ref.split( '.' ):
    val = val[key]
  return val