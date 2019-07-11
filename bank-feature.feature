Feature: BankFeature

  Scenario: Go to WWW refresh then go to BB refresh
    Given I navigate to BOI homepage
    When I click the accept cookie button
    And I refresh the page
    And I navigate to BB homepage
    When I click the accept cookie button
    And I refresh the page


