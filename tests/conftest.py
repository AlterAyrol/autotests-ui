import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=True)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()
    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")
    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")
    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")
    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")
    # Закрываем браузер
    browser.close()


@pytest.fixture
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()
    yield page
    browser.close()

