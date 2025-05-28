from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем, что отображается страница с заголовком "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        # Проверяем, что отображается иконка с папкой
        empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        # Проверяем, что отображается блок с текстом "There is no results"
        empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_view_title).to_be_visible()
        expect(empty_view_title).to_have_text('There is no results')

        # Проверяем, что отображается блок с текстом "Results from the load test pipeline will be displayed here"
        empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_view_description).to_be_visible()
        expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')
