#######################################################################################################################
# To construct json data template and to compare the values
#
# TODO#
# Mapper is not done completely.
# In mapper, values returned by value creator should be mapped to the data template created
# by TemplateCreator and then returned as expected JSON.
#
# __author__  = "empqtut"
# __version__ = "1.0.dev1"
# __email__   = "manikandan.chandrasekaran@ericsson.com"
# __status__  = "Development"
#######################################################################################################################
import _utils
import cilKeyReference
from queryManager import DatabaseHandler,result_formatter


class TemplateCreator:
    """
    class to create a json data template from the json schema
    """

    def __init__(self):
        pass

    def type_object(self, json):
        """
        processes object types in json schema
        :param json:
        :return:
        """
        json_prop = _utils.json_prop_finder(json)
        d = {k: (self.switcher(v)) for k, v in json_prop.items()}
        return d

    @staticmethod
    def type_array():
        """
        processes array types in json schema, TODO# 'items' type handling can be added in future
        :return:
        """
        return []

    @staticmethod
    def type_others():
        """
        processes string types in json schema, special string handling can be added in future
        :return:
        """
        return "<string>"

    def switcher(self, json_data):
        """
        logic handler for basic data types in json schema
        :param json_data:
        :return:
        """
        if json_data['type'] == "object":
            return self.type_object(json_data)
        elif json_data['type'] == "array":
            return self.type_array()
        elif json_data['type'] in ["string", "boolean", "numbers"]:
            return self.type_others()
        else:
            raise Exception("No basic types found in JSON schema")


class ValueCreator:
    """ class to create a json data template from the json schema """

    def __init__(self):
        self.vc_db_handle = DatabaseHandler()

    @staticmethod
    def sid_name_error(sid_name):
        """
        error handler for sid reference name in the reference file.
        :param sid_name:
        """
        if sid_name in cilKeyReference.sid_soi_reference:
            pass
        else:
            raise Exception("No reference for \"{0}\" in cilKeyReference.py".format(sid_name))

    def get_db_values(self, sid_name, **kwargs):
        """
        method to get expected values from database
        :param sid_name:
        :param kwargs:
        :return:
        """
        self.sid_name_error(sid_name)
        expected_data = {}
        local_sid_ref = cilKeyReference.sid_soi_reference[sid_name]
        for key in local_sid_ref.keys():
            if key not in cilKeyReference.referencecommands:
                expected_data.update(self.vc_db_handle.controller(key, **kwargs))
            else:
                pass
        return expected_data


class Mapper:
    """
        class to map values from DB with the json data template
    """

    def __init__(self):
        self.create_template = TemplateCreator()
        self.create_value = ValueCreator()
        self.json_expected = {}

    def get_data_template(self, schema_uri):
        """
        method to get json data template from the json schema url
        :param schema_uri:
        :return:
        """
        json_schema = _utils.read_json_schema_from_url(schema_uri)
        j_data_template = self.create_template.switcher(json_schema)
        return j_data_template

    def expected_json_builder(self, j_data, j_template):
        """
        method to build expected json from the DB values and the json data template
        to be improved in future
        :param j_data:
        :param j_template:
        """
        pass

    def json_mapper(self, sid_ref_id, json_schema_url, **kwargs):
        """
        method to control the logical flow of expected json creation
        :param sid_ref_id:
        :param json_schema_url:
        :param kwargs:
        """
        expected_json_values = self.create_value.get_db_values(sid_ref_id, **kwargs)
        json_data_template = self.get_data_template(json_schema_url)
        return result_formatter(expected_json_values,reference=cilKeyReference.sid_soi_reference)
