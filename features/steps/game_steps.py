from time import sleep

from behave import given, when, then


@given('user is on https://sylwia-wozniak.github.io/works/game/')
def step_start_page(context):
    context.driver.get("https://sylwia-wozniak.github.io/works/game/")


@given('user clicks the button \'get started\'')
def step_start_game(context):
    context.driver.find_element_by_css_selector('span.start').click()


@when('user clicks the ball {number:d} times')
def step_game(context, number):
    element = context.driver.find_element_by_css_selector('.ball')
    for i in range(1, number):
        element.click()
        sleep(1)
    sleep(22 - number)
    context.driver.save_screenshot('screenshot-game{}.png'.format(number))


@then('{result}')
def step_result_game(context, result):
    assert context.driver.find_element_by_css_selector('.final-score')
