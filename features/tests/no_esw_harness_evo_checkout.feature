# Created by rshche at 5/26/21

Feature: Test eSW Checkout UX for Norway Countries in Test Environment

  Scenario: Evo Checkout UX is invoked
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    Then Verify if EVO Checkout is invoked

  Scenario: Verify if the SLSQ order can be placed
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Enter all shipping info for NO
    And Select delivery method - Standard
    And Confirm billing info
    And Enter payment details
    And Submit an order
    Then Verify if Order Confirmation page is displayed

  Scenario: Verify if the SLMQ order can be placed
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Select QTY - 2
    And Enter Checkout
    Then Verify quantity in Checkout is correct
    When Enter all shipping info for NO
    And Select delivery method - Standard
    And Confirm billing info
    And Enter payment details
    And Submit an order
    Then Verify if Order Confirmation page is displayed
    And Verify quantity is correct on confirmation page

  Scenario: Verify if the MLSQ order can be placed
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 3; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    Then Verify if correct number of products is displayed
    When Enter all shipping info for NO
    And Select delivery method - Standard
    And Confirm billing info
    And Enter payment details
    And Submit an order
    Then Verify if Order Confirmation page is displayed
    And Verify if correct number of products is displayed

  Scenario: Verify if the MLMQ order can be placed
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 3; XA/XP - XP
    And Select country - Norway
    And Select QTY - 3
    And Enter Checkout
    Then Verify if correct number of products is displayed
    And Verify quantity in Checkout is correct
    When Enter all shipping info for NO
    And Select delivery method - Standard
    And Confirm billing info
    And Enter payment details
    And Submit an order
    Then Verify if Order Confirmation page is displayed
    And Verify if correct number of products is displayed
    And Verify quantity is correct on confirmation page

  Scenario: Verify if Become Member functionality is working properly
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Click "Become Member" CTA
    And Enter new member details and submit
    Then Verify if consumer is in logged-in state

  Scenario: Verify if Login functionality is working properly
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    And Click "Login" CTA
    When Enter Member details and submit
    Then Verify if consumer is in logged-in state

  Scenario: Verify if Member login invokes saved address
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Click "Login" CTA
    And Enter old Member details and submit
    Then Verify saved address is invoked
    When Click Continue
    And Select delivery method - Standard
    And Confirm billing info
    Then Verify Member card presence

  Scenario: Verify EDDs are consistent on the page
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Enter all shipping info for NO
    Then Verify EDDs are matching

  Scenario: Verify if consumer can't proceed without entering all required info
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Enter NOT all shipping info for NO
    Then Verify if Continue button is inactive
    When Enter missing shipping info for NO
    Then Verify if Continue button is clickable

  Scenario: Verify if billing address is empty when unchecked
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    When Enter all shipping info for NO
    And Select delivery method - Standard
    When Uncheck the Billing info box
    Then Verify the Billing address is empty

  Scenario: Verify if calculations are correct in subtotal
    Given Enter eSW test harness
    When Select end-point - SIT76
    And Select JSON: Number of lines - 1; XA/XP - XP
    And Select country - Norway
    And Enter Checkout
    Then Verify if calculations in Subtotal are correct


  Scenario: Verify Orders dropped into CSP
    Given Enter eSW CSP tool on SIT76
    When Open Customer Service page
    Then Search for order and verify it is in CSP