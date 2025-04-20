from selene import browser, be, have


def test_authorization_success():
    browser.open('http://the-internet.herokuapp.com/login')
    browser.element('[name="username"]').type('tomsmith')
    browser.element('[name="password"]').type('SuperSecretPassword!')
    browser.element('[type="submit"]').click()
    browser.element('div.example').should(have.text('Secure Area'))


def test_authorization_password_failure():
    browser.open('http://the-internet.herokuapp.com/login')
    browser.element('[name="username"]').type('tomsmith')
    browser.element('[name="password"]').type('wrong_password')
    browser.element('[type="submit"]').click()
    browser.element('div.error').should(have.text('Your username is invalid!'))
