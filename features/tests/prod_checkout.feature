# Created by rshche at 12/14/20
Feature: Test eSW Checkout UX for GS Countries in PROD


  Scenario: Verify Evo checkout is invoked
    Given Open Nike.com for Canada
    When Open any category
    And Select any Product
    And Select Size and add to Cart
    When Go to Cart
    And Proceed to Checkout as Guest
    Then Verify if EVO Checkout is invoked

  Scenario: Verify if the SLSQ order can be placed
    Given Open Nike.com for Canada
    When Open any category
    And Select any Product
    And Select Size and add to Cart
    When Go to Cart
    And Proceed to Checkout as Guest
    When Enter all shipping info
    And Select delivery method - Standard
    And Confirm billing info
    And Enter payment details
    Then Verify if "Place Order" button is enabled


  Scenario: Verify if calculations are correct in subtotal
    Given Open Nike.com for Canada
    When Open any category
    And Select any Product
    And Select Size and add to Cart
    When Go to Cart
    And Proceed to Checkout as Guest
    Then Verify if calculations in Subtotal are correct
