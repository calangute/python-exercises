#######################################################################################################################
# This Keyword Library is to test the MBEAN attributes of cache implemented in DIL Layer
#
# Test Dependencies:
#         Agent WAR  : Jolokia 1.3.3  (https://jolokia.org/agent/war.html)
#         Python Lib : pyjolokia 0.3.1
#
#  - Jolokia agent should be deployed in the same web-server where the application under test is deployed.
#      Agent WAR will be available under /mpde/common.x/ on all servers.
#    During build installation,	Copy jolokia war to the Tomcat webapps directory of BSCS/CBIO installation.
#
#             "cp -f /mpde/common.x/jolokia-war-1.3.3.war $CATALINA_HOME/webapps/jolokia.war"
#
#  - Install Python Jolokia Client with pip : pip install pyjolokia 0.3.1
#
# Test Suite Reference:
#   GIT_main\lhsj_main\bscs\tests\robotScripts\src\main\testcases\3__mainTests\restService\basic\DIL\CacheTest.robot
#######################################################################################################################

import json

from pyjolokia import Jolokia
from robot.libraries.BuiltIn import BuiltIn

builtin = BuiltIn()


def value_checker(value_before, value_after):
    """Takes before and after hit values and checks for count increment
    :param value_before: attribute value before the request
    :param value_after: attribute value after the request
    """
    value_expected = value_before + 1
    if not value_after == value_expected:
        raise RuntimeError("Value NOT incremented from {0} to {1} after the request!".format(value_before, value_expected))
    else:
        return True


def clear_dil_cache(url):
    """Performs removeALL() operation in the DIL cache Mbean - (clears eh cache)
     Test Suite variable ${mbean_cache} is used to access mbean attribute type "cache"
     :param url: Jolokia Agent URL installed in the web-server under test.
                Example : http://rome.lhs-systems.com:29001/jolokia/
    """
    j_url = Jolokia(url)
    j_response = j_url.request(type='exec', mbean=builtin.get_variable_value("${mbean_cache}"), operation='removeAll()')
    if j_response.get('status') != 200:
        raise RuntimeError("Jolokia response status is not 200, please check response!!")
    return json.dumps(j_response, indent=4)


def get_cache_hit(url):
    """Returns cache hit attribute value from the DIL cache Mbean
    Test Suite variable ${mbean_cache_stats} is used to access mbean attribute type "CacheStatistics"
    :param url: Jolokia Agent URL installed in the web-server under test.
                Example : http://rome.lhs-systems.com:29001/jolokia/
    """
    j_url = Jolokia(url)
    j_response = j_url.request(type='read', mbean=builtin.get_variable_value("${mbean_cache_stats}"), attribute='CacheHits')
    if j_response.get('status') != 200:
        raise RuntimeError("Jolokia response Status is not 200, please check response!!")
    print json.dumps(j_response, indent=4)
    return j_response.get('value')


def get_on_disk_miss(url):
    """Returns on disk miss attribute value from the DIL cache Mbean
    Test Suite variable ${mbean_cache_stats} is used to access mbean attribute type "CacheStatistics"
    :param url: Jolokia Agent URL installed in the web-server under test.
                Example : http://rome.lhs-systems.com:29001/jolokia/
    """
    j_url = Jolokia(url)
    j_response = j_url.request(type='read', mbean=builtin.get_variable_value("${mbean_cache_stats}"), attribute='OnDiskMisses')
    if j_response.get('status') != 200:
        raise RuntimeError("Jolokia response Status is not 200, please check response!!")
    print json.dumps(j_response, indent=4)
    return j_response.get('value')

