#CustomDB.py
from DatabaseLibrary import DatabaseLibrary
from robot.libraries.BuiltIn import BuiltIn


class CustomDB(DatabaseLibrary):
    """
    Custom DB class handling. This class is n   ecessary in order to have a better handling of the result of queries.
    In python it is not possible to access something like "result[0]['coid']" and 
    to make this better few methods had to be overwritten
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def custom_connect_to_database(self, dbapiModuleName, db_connect_string):
        """
        Calls the databaselibrary connection method with the givin parameters
        """
        self.connect_to_database_using_custom_params(dbapiModuleName, db_connect_string)

    def do_query(self,statement):
        """
        Executes a statement and before returning, adds a new line on the matrix where all the descriptions are added.
        Example how the returned matrix would look like:
        
        | BILLCYCLE | VALID_FROM | APPROVED_IND |
        | 01 | 04.04.2005 | X |
        | 02 | 14.09.2012 | X |
        | 03 | 02.10.2012 | X |
        
        """
        try:
            cursor = self._dbconnection.cursor()
            resultSet = cursor.execute(statement).fetchall()
            resultDesc = cursor.description
            matrix = []
            matrix.append([])
            
            for desc in resultDesc:
                matrix[0].append(desc[0])
            i=1
            for result in resultSet:
                matrix.append([])
                matrix[i].append(result)
                i += 1
            return matrix
        finally :
            if cursor :
                self._dbconnection.rollback() 

    def get_result_length(self, resultSet):
        """
        As it was added a new line due to descriptions, 
        this method returns the size of the resultSet -1
        """
        return str(len(resultSet)-1)
                
    def get_single_element(self, matrix, rowIndex, field):
        """
        The method loops over the matrix and return the value using the given 
        field and index
        """
        column = matrix[0]
        value = matrix[int(rowIndex) + 1]
        i = 0
        for columnName in column:
            if (columnName.lower() == field.lower()):
                returnStr = str(value[0][i])
                if(returnStr == "None"):
                    returnStr = "null";
                return returnStr
            i+=1

    def get_element_as_list(self, matrix, field):
        """
        This method returns a list containing all the result values for the given field
        """
        returnList = []
        column = matrix[0]
        i = 0
        for columnName in column:
            if (columnName.lower() == field.lower()):
                for j in range(1,len(matrix)):
                    value = matrix[j]
                    returnList.append(value[0][i])
                return returnList
            i+=1