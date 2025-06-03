import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill('user.name@gmail.com', 'username', 'password')
    registration_page.registration_form.check_visible('user.name@gmail.com', 'username', 'password')
    registration_page.click_registration_button()
    dashboard_page.toolbar_view.check_visible()

