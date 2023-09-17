#from playwright.sync_api import expect
import pytest
import pages


class Test_auth_page:

    def test_positive_auth(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.insert_login(page)
        pages.index_page.insert_password(page)
        pages.index_page.button_click(page)
        pages.index_page.wait_for_visible_after_logon(page)
        actual_result = pages.index_page.wait_for_visible_after_logon(page)
        assert actual_result == 'Персональные данные | Юрта - личный кабинет жителя'

    def test_negative_auth(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.insert_incorrect_login(page)
        pages.index_page.insert_incorrect_password(page)
        pages.index_page.button_click(page)
        pages.index_page.wait_for_uncorrect_data(page)
        actual_result_before_negative_auth = pages.index_page.check_notice_uncorrect_data(page)
        assert actual_result_before_negative_auth == "Объект содержит поле с недопустимым значением"

    def test_only_login(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.insert_login(page)
        pages.index_page.button_click(page)

    def test_registration(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.reg_button_click(page)
        pages.index_page.wait_for_registration_form(page)
        actual_result = pages.index_page.check_registration_form(page)
        assert actual_result == "Фамилия*"

    def test_service_providers(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.link_service_provider_click(page)
        pages.index_page.wait_for_visible_servise_providers(page)
        actual_result = pages.index_page.wait_for_visible_servise_providers(page)
        assert actual_result == "Авторизация | CRM"


