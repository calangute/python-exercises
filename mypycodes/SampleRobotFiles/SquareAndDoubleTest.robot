*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test title
    [Tags]    DEBUG
    ${x}=     set variable        ${4}
    ${y}=     Run keyword if     ${x}>0       square     ${x}
              ELSE IF   ${x}<=0         double       ${x}

*** Keywords ***
double
    [Arguments]    x
    $(result}=      evaluate     2*${x}
    return      ${result}

square
    [Arguments]    x
    $(result}=      evaluate     pow(${x},2)
    return      ${result}
