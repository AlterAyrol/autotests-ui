import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from tools.logger import get_logger
from elements.base_element import BaseElement


logger = get_logger("BUTTON")  # Инициализируем logger


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"


    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()
        # После успешной enabled проверки фиксируем покрытие как действие ENABLED
        self.track_coverage(ActionType.ENABLED, nth, **kwargs)


    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()
        # После успешной disabled проверки фиксируем покрытие как действие DISABLED
        self.track_coverage(ActionType.DISABLED, nth, **kwargs)
