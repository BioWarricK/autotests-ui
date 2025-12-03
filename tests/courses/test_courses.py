import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.upload_image_widget.upload_image("./testdata/files/image.png")
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            course_title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible('QAtest')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.upload_image_widget.upload_image("./testdata/files/image.png")
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Test course",
            estimated_time="2 days 12 hours",
            description="Test course",
            max_score="100",
            min_score="1"
        )
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            course_title='Test course',
            max_score='100',
            min_score='1',
            estimated_time='2 days 12 hours'
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Python',
            estimated_time='7 days',
            description='Python course',
            max_score='50',
            min_score='10'
        )
        create_course_page.course_toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            course_title='Python',
            max_score='50',
            min_score='10',
            estimated_time='7 days'
        )
