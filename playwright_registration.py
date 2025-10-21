from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = page.get_by_test_id('registration-form-email-input').locator('input')
    email_field.fill('qa_test@gmail.com')

    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('QAtest')

    password_field = page.get_by_test_id('registration-form-password-input').locator('input')
    password_field.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    header_visible = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(header_visible).to_be_visible()
    expect(header_visible).to_have_text('Dashboard')

    page.wait_for_timeout(5000)
