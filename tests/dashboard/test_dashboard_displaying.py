import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        # Проверяем, что компонент Navbar корректно отображается на странице
        dashboard_page_with_state.navbar.check_visible("username")
        # Проверяем, что компонент Sidebar виден и корректно отрисован.
        dashboard_page_with_state.sidebar.check_visible()
        # проверяем страницу
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
