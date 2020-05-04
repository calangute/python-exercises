*** Settings ***
Suite Setup    Run Keywords    Open SSH Connection
Suite Teardown    Run Keywords    Close All Connections
Library    SSHLibrary

*** Variables ***

*** Test Cases ***

test1
    [documentation] 
    [tag]
    ${index_rome}    Open Connection    rome.lhs-systems.com    prompt=$    alias=rome1
    Login    systch1    ChTeam123
    ${index_rivola}    Open Connection    rivola.lhs-systems.com    prompt=$
    #Execute Command    export ROBOT="robot"
    #Write   echo $ROBOT
    #Read Until Prompt
    log    ${index_rome}
    log    ${index_rivola}
    
    
test2
    ${index}    Open Connection    rome.lhs-systems.com    prompt=$    alias=rome
    Login    systch1    ChTeam123
    Write    ssh systch1@rivola.lhs-systems.com
    ${op}    Read Until    :
    should contain    ${op}    systch1@rivola.lhs-systems.com's password
    write    ChTeam123
    New Keyword
    # Read until    $
    # write    uname -a
    # Read until    $
    


*** Keywords ***
New Keyword
	[arguments] arg1    arg2    arg3=${EMPTY}
	[documentation] consumes arg1 arg2 and arg3 and returns a new customer id
	step1
	...
	..
	..
	[return] ${customerId}