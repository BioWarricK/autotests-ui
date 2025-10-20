from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('user.name@gmail.com')

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('password')

    login_button_click = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button_click.click()

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)



#CSS локаторы для того же теста

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_field = page.get_by_test_id('login-form-email-input').locator('input')
    email_field.fill('username@gmail.com')

    password_field = page.get_by_test_id('login-form-password-input').locator('input')
    password_field.fill('password')

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(alert).to_be_visible()
    expect(alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)

