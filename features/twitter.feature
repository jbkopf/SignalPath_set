Feature: test twitter

  Scenario: go to twitter
    Given I go to https://www.twitter.com/login
    When I login to twitter setting remember me to no
    And I reset the browser for twitter
    Then I go with cookies to https://www.twitter.com
    And I see I am not logged in
    And I go to https://www.twitter.com/login
    When I login to twitter setting remember me to yes
    And I reset the browser for twitter
    Then I go with cookies to https://www.twitter.com
    And I see I am logged in
