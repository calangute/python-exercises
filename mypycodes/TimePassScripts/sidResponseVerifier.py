from robot.libraries.BuiltIn import BuiltIn,register_run_keyword
import RequestsLibrary
'''
keyword to verify keys/values of the JSON reponse from SID like REST in DIL by comparing it with CIL REST response

Note : This can be only used for comparing SID like REST response with REST response from CIL
and validation of the REST response from CIL is out of scope for this keyword.
'''


def call_keyword(keyword, *args):
    """ calls robot's run keyword"""
    return BuiltIn().run_keyword(keyword, *args)


def create_comp_session(session_user, session_password, session_alias='dil'):
    """creates new HTTP session - not utilized yet in any test cases
    :param session_user: <user name for the session>
    :param session_password:<password for the session>
    :param session_alias:<alias name of the session>
    """
    auth = (session_user, session_password)
    session_create = RequestsLibrary.RequestsLibrary()
    return session_create.create_session(session_alias,"http://rome.lhs-systems.com:29001/dil/rest", auth=auth)

def verify_sid_response():
    """function to compare sid like response and the CIL response"""
    create_comp_session("AUT", "AUT")
    result = register_run_keyword(__name__, call_keyword('Execute Rest Command',"/CIL/6/ADDRESS.READ","Get",200))
    print result
    return result
# call_keyword('Execute Rest Command',["/CIL/6/ADDRESS.READ","Get",200])