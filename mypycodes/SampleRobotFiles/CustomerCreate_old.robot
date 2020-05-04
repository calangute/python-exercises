*** Settings ***
Documentation     Suite to test REST response of CUSTOMER.CREATE command.
Suite Setup       Run Keywords    Set Suite Variable    ${customercreate}    /CIL/6/CUSTOMER.CREATE
...               AND    Set Suite Variable    ${session_alias}    bscs
Library          ../../../../../keywords/webService/compositeCommands.py
Library          Collections

*** Test Cases ***
Status Check
    [Tags]    c45aa_e1
    ${data}=    Set Variable    ${CURDIR}/../../resources/CustomerCreate/customerCreate.json
    ${resp}=    status checker     ${customercreate}    Post    ${data}
    Should be equal    ${resp}    ${200}

Post Request
    [Tags]    c45aa_e1
    ${data}=    Set Variable    ${CURDIR}/../../resources/CustomerCreate/customerCreate.json
    ${resp}=    execute composite command    ${customercreate}    Post    ${data}
    ${content}=      Get From Dictionary    ${resp["content"]}    customerNew
    ${csId}=         Get From Dictionary    ${content}    csId
    ${csCreationDate}=      Get From Dictionary    ${content}    csCreationDate
    Should Be Equal As Strings    ${resp["status"]}    200
    Should Not Be Equal           ${csId}              ${EMPTY}
    Should Not Be Empty           ${csCreationDate}

Put Request
    [Tags]    c45aa_e1
    ${data}=    Set Variable    ${CURDIR}/../../resources/CustomerCreate/customerCreate.json
    ${resp}=    execute composite command    ${customercreate}    Put    ${data}
    ${content}=      Get From Dictionary    ${resp["content"]}    customerNew
    ${csId}=         Get From Dictionary    ${content}    csId
    ${csCreationDate}=      Get From Dictionary    ${content}    csCreationDate
    Should Be Equal As Strings    ${resp["status"]}    200
    Should Not Be Equal           ${csId}              ${EMPTY}
    Should Not Be Empty           ${csCreationDate}


