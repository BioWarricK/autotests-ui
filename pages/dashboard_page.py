from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.dashboard_title_text = page.get_by_test_id('dashboard-toolbar-title-text')
        self.students_widget_text = page.get_by_test_id('students-widget-title-text')
        self.activities_widget_text = page.get_by_test_id('activities-widget-title-text')
        self.courses_widget_text = page.get_by_test_id('courses-widget-title-text')
        self.scores_widget_text =  page.get_by_test_id('scores-widget-title-text')
        self.dashboard_button = page.get_by_test_id('dashboard-drawer-list-item-button')
        self.courses_button = page.get_by_test_id('courses-drawer-list-item-button')
        self.logout_button = page.get_by_test_id('logout-drawer-list-item-button')
        self.navbar_title_text = page.get_by_test_id('navigation-navbar-app-title-text')
        self.navbar_welcome_text = page.get_by_test_id('navigation-navbar-welcome-title-text')
        self.students_chart = page.get_by_test_id('students-bar-chart')
        self.activities_chart = page.get_by_test_id('activities-line-chart')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')


    def check_dashboard_title_text(self):
        """
        Проверка видимости и наличия текста в заголовке
        """
        expect(self.dashboard_title_text).to_be_visible()
        expect(self.dashboard_title_text).to_have_text('Dashboard')