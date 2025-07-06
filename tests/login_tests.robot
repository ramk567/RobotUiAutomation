*** Settings ***
Documentation    Login functionality tests
Resource         ../resources/common.resource
Library          ../pages/login_page.py
Test Setup       Setup Test Environment
Test Teardown    Teardown Test Environment
Test Tags        login    smoke

*** Variables ***
${VALID_USERNAME}      admin@example.com
${VALID_PASSWORD}      password123
${INVALID_USERNAME}    invalid@example.com
${INVALID_PASSWORD}    wrongpassword

*** Test Cases ***
Valid Login Test
    [Documentation]    Test login with valid credentials
    [Tags]    positive    critical
    Navigate To    ${BASE_URL}/login
    Verify Login Form Visible
    Login With Credentials    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verify Login Success

Invalid Username Test
    [Documentation]    Test login with invalid username
    [Tags]    negative
    Navigate To    ${BASE_URL}/login
    Verify Login Form Visible
    Login With Credentials    ${INVALID_USERNAME}    ${VALID_PASSWORD}
    Verify Error Message Displayed

Invalid Password Test
    [Documentation]    Test login with invalid password
    [Tags]    negative
    Navigate To    ${BASE_URL}/login
    Verify Login Form Visible
    Login With Credentials    ${VALID_USERNAME}    ${INVALID_PASSWORD}
    Verify Error Message Displayed

Empty Credentials Test
    [Documentation]    Test login with empty credentials
    [Tags]    negative
    Navigate To    ${BASE_URL}/login
    Verify Login Form Visible
    Click Login Button
    Wait For Element Visible    //div[contains(text(), 'required')]

Multiple Invalid Attempts Test
    [Documentation]    Test multiple invalid login attempts
    [Tags]    security
    Navigate To    ${BASE_URL}/login
    FOR    ${i}    IN RANGE    3
        Login With Credentials    ${INVALID_USERNAME}    ${INVALID_PASSWORD}
        Verify Error Message Displayed
        Sleep    1s
    END
