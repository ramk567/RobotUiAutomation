*** Settings ***
Library    SeleniumLibrary
Library    keywords.common_keywords.CommonKeywords
Library    pages.base_page.BasePage
Library    RequestsLibrary
Library    Collections
Library    String
Library    DateTime
Library    OperatingSystem

*** Variables ***
${BROWSER}              chrome
${HEADLESS}             False
${TIMEOUT}              10
${IMPLICIT_WAIT}        5
${BASE_URL}             https://staging2.nimblethis.net
${SCREENSHOT_DIR}       screenshots
${REPORTS_DIR}          reports

*** Keywords ***
Setup Test Environment
    [Documentation]    Setup test environment
    Create Directory    ${SCREENSHOT_DIR}
    Create Directory    ${REPORTS_DIR}
    Setup Browser    ${BROWSER}    ${HEADLESS}

Teardown Test Environment
    [Documentation]    Teardown test environment
    Run Keyword If Test Failed    Take Screenshot On Failure
    Close All Browsers

Open Application
    [Documentation]    Open the application
    Navigate To    ${BASE_URL}
    Wait For Page To Load

Login As User
    [Documentation]    Login as a user
    [Arguments]    ${username}    ${password}
    Navigate To    ${BASE_URL}/login
    Login With Credentials    ${username}    ${password}

Verify Login Success
    [Documentation]    Verify successful login
    Verify Url Contains    dashboard
    Wait For Element Visible    //h1[contains(text(), 'Dashboard')]

Generate Random Email
    [Documentation]    Generate random email for testing
    [Return]    ${email}
    ${email}=    Generate Test Data    email
    RETURN    ${email}

Wait And Click Element
    [Documentation]    Wait for element and click
    [Arguments]    ${locator}    ${timeout}=10
    Wait For Element Visible    ${locator}    ${timeout}
    Click Element    ${locator}

Wait And Input Text
    [Documentation]    Wait for element and input text
    [Arguments]    ${locator}    ${text}    ${timeout}=10
    Wait For Element Visible    ${locator}    ${timeout}
    Clear Element Text    ${locator}
    Input Text    ${locator}    ${text}
