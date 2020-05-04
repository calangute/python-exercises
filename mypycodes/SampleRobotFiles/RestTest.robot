*** Settings ***
Library           Collections
Library           requests
Library           RequestsLibrary
Library           OperatingSystem
Library           json
Variables         variables.py
Library           json_test.py

*** Test Cases ***
Test1
    ${auth}=    Create List    ${USER}    ${PASSWORD}
    ${params}=  Create Dictionary  csId=29
    Create Session    bscs    ${RESTURL}    auth=${auth}
    ${result}=    get request    bscs    /CIL/6/CUSTOMER.READ   params=${params}
    Should Be Equal    ${result.status_code}    ${200}
    ${json}=    Set Variable    ${result.json()}
    json_value_equal_check    ${json}    csIdPub    CUST0000000002
    json_value_equal_check    ${json}    csStatus    a
    json_check    29


*** Keywords ***
json_value_equal_check
    [Arguments]    ${json}    ${property}    ${value_expected}
    ${value_found}=    Get From Dictionary    ${json}    ${property}
    ${error_message}=    Catenate    Expected value of '${property}' was '${value_expected}' but found    '${value_found}'
    Should Be Equal As Strings    ${value_expected}    ${value_found}    ${error_message}    values=False
