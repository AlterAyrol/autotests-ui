import pytest
from playwright.sync_api import expect, sync_playwright


@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")],
    ids=[
    "Invalid email and password",
    "Invalid email and empty password",
    "Empty email and invalid password"
])
def test_wrong_email_or_password_authorization(email: str, password: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Переходим на страницу
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Заполняем поле email
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)
        # Заполняем поле пароль
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)
        # Нажимаем на кнопку Login
        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()
        # Проверяем сообщение об ошибке
        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

