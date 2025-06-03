import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', "Title")
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', "Create course")


    def check_visible(self, is_create_course_disabled: bool = True):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        self.check_current_url(re.compile(".*/#/courses"))
