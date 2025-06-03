from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    def check_enabled(self, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled()
