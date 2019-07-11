Feature: Search


#  Scenario: Search PyPI
#    Given I open BOI homepage
#    When I click the cookie accept button
#    And I search for "cards"

  Scenario: Search BB
    Given I navigate to BB homepage
    When I click the accept cookie button
    And I search for "Business Current Account"
    Then I check the BCA Features url is in the results

  # DO A SEARCH FOR CORRECT URL, TEXT ON BB PAGE, LOOK UP GIT AND CHECK GIT EXPLAINED, SOURCE CONTROL (WAY OF SAVING YOUR WORK WHEN MANY PEOPLE WORKING ON SAME THING)

#  Scenario: Verify mega menu functionality
#    Given I navigate to BOI homepage
#    When I click the Cookie accept button
#    And I click products in the mega menu
#    Then Mortgages tab appears
#    When I click "Services" in mega menu
#    Then "Current account services" is visible



    #'And' will mimick the step before, only use when string is same

    #'behave feature.feature' (in terminal to run)

    #add cookie click and send enter to search field, and command and slash for section comment, ls shows current directory, cd changes directory, cd.. moves back one, cd ~ brings back to beginning

    #HOMEWORK: On homepage, open megamenu and verify that mortgages is displayed and (use assertion) then click services and finanial wellbeing is displayed