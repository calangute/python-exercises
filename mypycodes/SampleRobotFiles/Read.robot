*** Settings ***
Suite Teardown    Delete All Sessions
Resource          ../../../../../keywords/restService/common.txt
Library           Collections
Library           String
Library           OperatingSystem
Library           RequestsLibrary
Library           HttpLibrary
Variables         ../../../../ecc_variables.py

*** Test Cases ***
Get Request
    [Tags]    get
    ${resp}=    Execute Rest Command    /CIL/6/CURRENCIES.READ    Get Request
    Log    ${resp.json()}
    Should Be Equal As Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${currencies}=    Get From Dictionary    ${json}    currencies
    ${currenciesResult}=    Get Length    ${currencies}
    : FOR    ${index}    IN RANGE    0    ${currenciesResult}
    \    ${currenciesResultListpartList}=    Get From List    ${currencies}    ${index}
    \    ${currencyId}=    Get From Dictionary    ${currenciesResultListpartList}    currencyId
    \    ${currencyIdPub}=    Get From Dictionary    ${currenciesResultListpartList}    currencyIdPub
    \    ${fcCode}=    Get From Dictionary    ${currenciesResultListpartList}    fcCode
    \    ${fcDesc}=    Get From Dictionary    ${currenciesResultListpartList}    fcDesc
    \    ${postDigits}=    Get From Dictionary    ${currenciesResultListpartList}    postDigits
    Log    ${currencyId},${currencyIdPub},${fcCode},${fcDesc},${postDigits}

Post Request
    [Tags]    post
    ${resp}=    Execute Rest Command    /CIL/6/CURRENCIES.READ    POST Request
    Log    ${resp.json()}
    Should Be Equal As Strings    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    ${currencies}=    Get From Dictionary    ${json}    currencies
    ${currenciesResult}=    Get Length    ${currencies}
    : FOR    ${index}    IN RANGE    0    ${currenciesResult}
    \    ${currenciesResultListpartList}=    Get From List    ${currencies}    ${index}
    \    ${currencyId}=    Get From Dictionary    ${currenciesResultListpartList}    currencyId
    \    ${currencyIdPub}=    Get From Dictionary    ${currenciesResultListpartList}    currencyIdPub
    \    ${fcCode}=    Get From Dictionary    ${currenciesResultListpartList}    fcCode
    \    ${fcDesc}=    Get From Dictionary    ${currenciesResultListpartList}    fcDesc
    \    ${postDigits}=    Get From Dictionary    ${currenciesResultListpartList}    postDigits
    Log    ${currencyId},${currencyIdPub},${fcCode},${fcDesc},${postDigits}
