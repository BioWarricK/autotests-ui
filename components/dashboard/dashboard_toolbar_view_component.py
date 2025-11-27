from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self):
        expect(self.title_text).to_be_visible()
        expect(self.title_text).to_have_text('Dashboard')