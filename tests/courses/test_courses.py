import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.suite import AllureSuite
from tools.allure.parent_suite import AllureParentSuite
from tools.allure.sub_suite import AllureSubSuite
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.COURSES)
@allure.sub_suite(AllureSubSuite.COURSES)
class TestCourses:

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        courses_list_page.visit(AppRoute.CREATE_COURSE)
        # проверяем наличие заголовка "Create course" и что кнопка подтверждения создания курса недоступна для нажатия
        create_course_page.create_toolbar_view.check_visible()
        # проверяем, что отображается пустой блок для предпросмотра изображения
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        # проверяем, что форма создания курса отображается и содержит значения по умолчанию
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )
        # проверяем наличие заголовка "Exercises" и наличие кнопки создания задания
        create_course_page.exercises_toolbar_view.check_visible()
        # проверяем, что отображается блок с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()
        # загружаем изображение для превью курса
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        # проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        # заполняем форму создания курса
        create_course_page.create_course_form.fill(
            title="Playwright", estimated_time="2 weeks",
            description="Playwright", max_score="100", min_score="10"
        )
        # нажимаем на кнопку создания курса
        create_course_page.create_toolbar_view.click_create_course_button()
        # после редиректа на страницу со списком курсов, проверяем наличие заголовка и кнопки
        courses_list_page.toolbar_view.check_visible()
        # проверяем корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10",
            estimated_time="2 weeks"
        )


    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        # Переходим на страницу курсов
        courses_list_page.visit(AppRoute.MAIN_COURSE)
        # Проверяем, что компонент Navbar корректно отображается на странице
        courses_list_page.navbar.check_visible(username=settings.test_user.username)
        # Проверяем, что компонент Sidebar виден и корректно отрисован.
        courses_list_page.sidebar.check_visible()
        # Проверяем, что отображается страница с заголовком "Courses" и кнопки
        courses_list_page.toolbar_view.check_visible()
        # Проверяем, что отображается блок с отсутствием курсов
        courses_list_page.check_visible_empty_view()


    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        courses_list_page.visit(AppRoute.CREATE_COURSE)
        # загружаем изображение для превью курса
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        # проверяем, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        # заполняем форму создания курса
        create_course_page.create_course_form.fill(
            title="Playwright", estimated_time="2 weeks",
            description="Playwright", max_score="100", min_score="10"
        )
        # нажимаем на кнопку создания курса
        create_course_page.create_toolbar_view.click_create_course_button()
        # после редиректа на страницу со списком курсов, проверяем наличие заголовка и кнопки
        courses_list_page.toolbar_view.check_visible()
        # проверяем корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10",
            estimated_time="2 weeks"
        )
        # нажимаем кнопку edit через меню карточки курса
        courses_list_page.course_view.menu.click_edit(index=0)
        # заполняем отредактированную форму создания курса
        create_course_page.create_course_form.fill(
            title="New title", estimated_time="1 month",
            description="New playwright", max_score="70", min_score="20"
        )
        # нажимаем на кнопку создания курса для сохранения изменений
        create_course_page.create_toolbar_view.click_create_course_button()
        # после редиректа на страницу со списком курсов, проверяем наличие заголовка и кнопки
        courses_list_page.toolbar_view.check_visible()
        # проверяем корректность новых отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0, title="New title", max_score="70", min_score="20",
            estimated_time="1 month"
        )
