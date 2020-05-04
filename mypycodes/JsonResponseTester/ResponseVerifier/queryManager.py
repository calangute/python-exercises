######################################################################################################################
#
# to manage DB connections. uses CX_Oracle.
#
# __author__ = "empqtut"
# __version__ = "1.0.dev1"
# __email__ = "manikandan.chandrasekaran@ericsson.com"
# __status__ = "Development"
######################################################################################################################
import cx_Oracle
import os
import variables
import _utils
import logging
from tableReference import *


this_dir, this_filename = os.path.split(__file__)

def list_separator(func):
    """
    decorator to make a comma separated string from a list
    """

    def formatter(*args, **kwargs):
        """
        Wrapper function for the decorator
        """
        result_local = func(*args, **kwargs)
        output = ",".join(result_local)
        return output

    return formatter


def result_formatter(result_dict, reference=tableReference):
    """format the output by modifying the keys to sid_ref"""
    formatted_dict = {}
    for k_res, v_res in result_dict.items():
        for k_ref, v_ref in _utils.atomize_dict(reference).items():
            if k_res == v_ref and v_res is not None:
                formatted_dict[k_ref] = v_res
    return formatted_dict

class DatabaseHandler:
    """
    Handles the SQL construction and data retrieval from Database
    TODO # ORM can be used to implement this and faster data retrieval.
    """

    def __init__(self):
        self.db_handle = self.db_connector(variables.DBHOST, variables.DBPORT, variables.DBSID)

    @staticmethod
    def db_connector(host, port, sid):
        """
        Manages DB connection by creating local dsn
        :param host: database host
        :param port: database port
        :param sid: database SID
        :return: connection object for the DB with the input parameters
        """
        logging.info('Connecting using : CX_Oracle.connect(database=%s, host=%s, port=%s, user=%s, password=%s) ' % (
            sid, host, port, variables.DBUSERNAME, variables.DBPASSWORD))
        dsn_db = cx_Oracle.makedsn(host, port, sid)
        db_conn = cx_Oracle.connect(variables.DBUSERNAME, variables.DBPASSWORD, dsn_db)
        return db_conn

    @staticmethod
    def select(table_name, columns, **kwargs):
        """
        Builds a select statement, this can be extended to build other DML statements as well.
        :param table_name:
        :param columns:
        :param kwargs:
        :return:
        """
        query_list = list()
        query_list.append("SELECT {0} FROM {1} ".format(columns, table_name))
        if kwargs:
            query_list.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
        return "".join(query_list)

    @list_separator
    def db_elements_extractor(self, soi_command, element_name):
        """
        extracts tables,row and column details from the reference file, element_name name corresponds
        to the element_name to be returned
        :param soi_command:
        :param element_name:
        :return:
        """
        table_names = [key for key in tableReference[soi_command]]
        column_names = []
        key_names = []
        for a in table_names:
            dict_value = tableReference[soi_command][a].values()
            dict_keys = tableReference[soi_command][a].keys()
            key_names.extend([s for s in dict_keys])
            a = "{0}.".format(a)
            column_names.extend([a + s for s in dict_value])
        if element_name.lower() == 'tables':
            return table_names
        elif element_name.lower() == 'columns':
            return column_names
        elif element_name.lower() == 'sid_keys':
            return list(key_names)
        else:
            raise ValueError('"{0}" not matched with existing elements.Enter any one in ("tables","columns")'.format(element_name))

    def dml_statement_builder(self, command, **kwargs):
        """
        Builds sql statements, currently constructs only select statements, can be extended for further statements
        :param command:
        :return:
        """
        tables_list = self.db_elements_extractor(command, "tables")
        columns_list = self.db_elements_extractor(command, "columns")
        query = self.select(tables_list, columns_list, **kwargs)
        return query


    def query_executor(self, query):
        """Takes a query, creates a session and a cursor, executes it and returns the query value"""
        cursor = self.db_handle.cursor()
        cursor.execute(query)
        columns = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        query_result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        if len(query_result) > 1:
            return query_result
        else:
            return query_result[0]



    def controller(self, soicommand, **kwargs):
        """
        controls other function inside this class, main point of access from outside class
        :param soicommand:
        :return:
        """
        sql_statement = self.dml_statement_builder(soicommand, **kwargs)
        result = self.query_executor(sql_statement)
        # jsonified_result = json.dumps(result, indent=4, sort_keys=True)
        return result_formatter(result)

myobj = DatabaseHandler()
print myobj.controller('addressRead',**{"customer_id": "12", "CCBILL": 'X'})