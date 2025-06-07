import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.suite import AllureSuite
from tools.allure.parent_suite import AllureParentSuite
from tools.allure.sub_suite import AllureSubSuite
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.DASHBOARD)
@allure.sub_suite(AllureSubSuite.DASHBOARD)
class TestDashboard:

    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        # Проверяем, что компонент Navbar корректно отображается на странице
        dashboard_page_with_state.navbar.check_visible(username=settings.test_user.username)
        # Проверяем, что компонент Sidebar виден и корректно отрисован.
        dashboard_page_with_state.sidebar.check_visible()
        # проверяем страницу
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
