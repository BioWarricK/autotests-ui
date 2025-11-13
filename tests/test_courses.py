from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_text).to_be_visible()
        expect(title_text).to_have_text('Courses')

        courses_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list).to_be_visible()
        expect(courses_list).to_have_text('There is no results')

        courses_list_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_list_icon).to_be_visible()

        result_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_text).to_be_visible()
        expect(result_text).to_have_text('Results from the load test pipeline will be displayed here')
