*** Settings ***
Documentation     Suite to test REST response of CUSTOMER.CREATE command.
Suite Setup       Run Keywords    Set Suite Variable    ${customercreate}    /CIL/6/CUSTOMER.CREATE
...               AND    Set Suite Variable    ${session_alias}    bscs


*** Test Cases ***
Post Request
    [Tags]    SOIVERSION:CIL_6   c45aa_e1
    ${address_rad}=    Execute Rest Command     ${addressread}    Post    200    ${data}    2
    ${address_rad}=    Execute Rest Command     ${addressread}    Post    200    ${data}    2
    ${address_rad}=    Execute Rest Command     ${addressread}    Post    200    ${data}    2


Post Request
    [Tags]    SOIVERSION:CIL_6   c45aa_e1
    ${data}=    Get Input Data     ${CURDIR}/../../resources/CustomerCreate/customerCreate.json
    ${resp}=    Execute Rest Command     ${customercreate}    Put    200    ${data}    2
    ${custNew}=         Get From Dictionary    ${resp["content"]}    customerNew
    ${csId}=    Get From Dictionary    ${custNew}    csId
    ${csCreationDate}=      Get From Dictionary    ${custNew}    csCreationDate
    Should Not Be Equal           ${csId}              ${EMPTY}
    Should Not Be Empty           ${csCreationDate}


