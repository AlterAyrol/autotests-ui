import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    # проверяем наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    # проверяем, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    # проверяем, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    # проверяем, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view()
    # проверяем, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )
    # проверяем наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    # проверяем наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    # проверяем, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()
    # загружаем изображение для превью курса
    create_course_page.upload_preview_image(file="./testdata/files/image.png")
    # проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view()
    # заполняем форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright", estimated_time="2 weeks",
        description="Playwright", max_score="100", min_score="10"
    )
    # нажимаем на кнопку создания курса
    create_course_page.click_create_course_button()

    # после редиректа на страницу со списком курсов, проверяем наличие заголовка
    courses_list_page.check_visible_courses_title()
    # проверяем наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # проверяем корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10",
        estimated_time="2 weeks"
    )


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # Переходим на страницу курсов
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    # Проверяем, что компонент Navbar корректно отображается на странице
    courses_list_page.navbar.check_visible("username")
    # Проверяем, что компонент Sidebar виден и корректно отрисован.
    courses_list_page.sidebar.check_visible()
    # Проверяем, что отображается страница с заголовком "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверяем, что что кнопка для создания нового курса отображается
    courses_list_page.check_visible_create_course_button()
    # Проверяем, что отображается блок с отсутствием курсов
    courses_list_page.check_visible_empty_view()

