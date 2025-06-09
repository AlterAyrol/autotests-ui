import pytest
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)  # Добавляем параметризацию
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # Добавили аргумент request
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param  # Передаем браузер как параметр
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Запускаем Chromium браузер в обычном режиме (не headless)
    # Используем settings.headless
    browser = playwright.chromium.launch(headless=settings.headless)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    #  контексте используется get_base_url
    context = browser.new_context(base_url=settings.get_base_url())
    # Открываем новую страницу в рамках контекста
    page = context.new_page()
    # Переходим на страницу регистрации
    registration_page = RegistrationPage(page = page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,  # Используем settings.test_user.email
        username=settings.test_user.username,  # Используем settings.test_user.username
        password=settings.test_user.password  # Используем settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)  # Используем settings.browser_state_file
    browser.close()


@pytest.fixture(params=settings.browsers)  # Добавляем параметризацию
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:  # Добавили аргумент request
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,  # Передаем браузер как параметр
        storage_state=settings.browser_state_file  # Используем settings.browser_state_file
    )

