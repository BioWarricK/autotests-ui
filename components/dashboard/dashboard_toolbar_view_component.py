import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = Text(page, 'dashboard-toolbar-title-text', 'Title')

    @allure.step('Check visible dashboard toolbar view')
    def check_visible(self):
        self.title_text.check_visible()
        self.title_text.check_have_text('Dashboard')
