from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    # переход на страницу

    email_field = page.get_by_test_id('login-form-email-input').locator('input')
    email_field.focus()
    # фокус на поле ввода

    for character in 'user@gmail.com':
        page.keyboard.press(character, delay=300)
    #     ввод посимвольно с задержкой между нажатием 300мс

    page.keyboard.press('ControlOrMeta+A')
    # нажатие на клавиатуре ctrl + A для выделения всего текста или Command + A

    page.wait_for_timeout(5000)