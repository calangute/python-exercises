*** Settings ***
Documentation    Suite description
Library          var_test.py

*** Test Cases ***
Test title
    [Tags]    DEBUG
     ${y}     x calc    ${5}
