from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    # Переходим на страницу входа
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем, что отображается страница с заголовком "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверяем, что отображается иконка с папкой
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверяем, что отображается блок с текстом "There is no results"
    empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    # Проверяем, что отображается блок с текстом "Results from the load test pipeline will be displayed here"
    empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

