from playwright.sync_api import Page
import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.navbar.check_visible('QAtest')
    dashboard_page_with_state.check_dashboard_title_text()
    dashboard_page_with_state.check_visible_students_chart()
    dashboard_page_with_state.check_visible_courses_chart()
    dashboard_page_with_state.check_visible_scores_chart()
    dashboard_page_with_state.check_visible_activities_chart()