Feature: user plays the game
  User wins if he has 15 scores or more.
  First click is to start. It isn't score. To win user must clicks 16 times.
  Scenario Outline: user wins the game
    Given user is on https://sylwia-wozniak.github.io/works/game/
    And user clicks the button 'get started'
    When user clicks the ball <number> times
    Then <result>

    Examples:
    |number|result|
    |12   |game is over|
    |16   |user is the winner|
