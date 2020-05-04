*** Settings ***
Library    SSHLibrary


*** Test Cases ***
test1
    ${index}    Open Connection    rome.lhs-systems.com    prompt=$
    Login    systch1    ChTeam123
    Execute Command    export ROBOT="robot"
    Write   echo $ROBOT
    Read Until Prompt
    log    ${index}
    
    
test2
    ${index}    Open Connection    rome.lhs-systems.com    prompt=$    alias=rome
    Login    systch1    ChTeam123
    Write    ssh systch1@rivola.lhs-systems.com
    ${op}    Read Until    :
    should contain    ${op}    systch1@rivola.lhs-systems.com's password
    write    ChTeam123
    Read until    $
    write    uname -a
    Read until    $
    
    