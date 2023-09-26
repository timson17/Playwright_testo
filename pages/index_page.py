from playwright.sync_api import Page
import config


class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def insert_login(self, page: Page) -> None:
        page.locator(config.locators.LOGIN_INPUT).fill("89373176733")

    def insert_password(self, page: Page) -> None:
        page.locator(config.locators.PASSWORD_INPUT).fill("12345678")

    def insert_incorrect_login(self, page: Page) -> None:
        page.locator(config.locators.LOGIN_INPUT).fill("32748932489")

    def insert_incorrect_password(self, page):
        page.locator(config.locators.PASSWORD_INPUT).fill("3724672384")

    def button_click(self, page):
        page.locator(config.locators.ENTRY_BUTTON).click()

    def wait_for_visible_servise_providers(self, page):
        page.locator(config.locators.YAKOR_FOR_CHECK_SERVICE_PROVIDERS).wait_for(state="visible")
        return page.title()

    def wait_for_visible_after_logon(self, page):
        page.locator(config.locators.YAKOR_FOR_CHECK_LOGON).wait_for(state="visible")
        return page.title()

    def wait_for_uncorrect_data(self, page):
        page.locator(config.locators.NOTICE_BAD_DATA).wait_for(state="visible")

    def wait_for_registration_form(self, page):
        page.locator(config.locators.YAKOR_FOR_REGISTRATION_FORM).wait_for(state="visible")

    def wait_for_remind_password_form(self, page):
        page.locator(config.locators.REMIND_PASSWORD_AUTH_TITLE).wait_for(state="visible")

    def wait_for_redirect_app_store(self, page):
        page.locator(config.locators.YAKOR_FOR_CHECK_APP_STORE_REDIRECT).wait_for(state="visible")
        return page.title()

    def check_notice_uncorrect_data(self, page):
        return page.locator(config.locators.NOTICE_BAD_DATA).inner_text()

    def check_registration_form(self, page):
        return page.locator(config.locators.REGISTRATION_FORM_CHECK).inner_text()

    #Не знаю за что зацепится
    def check_popup_auth_form(self, page):
        return page.locator(config.locators.LOGIN_FORM).inner_text()

    def check_remind_password_form(self,page):
        return page.locator(config.locators.REMIND_PASSWORD_AUTH_TITLE).inner_text()

    def check_redirect_appstore(self, page):
        page.locator(config.locators.YAKOR_FOR_CHECK_REDIRECT_APPSTORE).wait_for(state="visible")

    def link_service_provider_click(self, page):
        page.locator(config.locators.SERVICE_PROVIDER_LINK).click()

    def registration_link_click(self, page):
        page.locator(config.locators.REMIND_PASSWORD_LINK).click()

    def reg_button_click(self, page):
        page.locator(config.locators.REGISTRATION_BUTTON).click()

    def link_app_store_click(self, page):
        page.locator(config.locators.APP_STORE_LINK).click()

    def app_store(self,page):
        with page.expect_popup() as page1_info:
            page.get_by_role("list").get_by_role("link").first.click()
        page1 = page1_info.value
        page1.get_by_role("heading", name="Юрта – личный кабинет жителя 4+").click()

    def app_gallery(self,page):
        with page.expect_popup() as page1_info:
            page.get_by_role("list").get_by_role("link").nth(2).click()
        page1 = page1_info.value
        page1.get_by_text("Юрта – личный кабинет жителя").click()

    def google_play (self,page):
        with page.expect_popup() as page1_info:
            page.get_by_role("list").get_by_role("link").nth(1).click()
        page1 = page1_info.value
        page1.get_by_text("Юрта – личный кабинет жителя").click()

    def about_yurta(self, page):
        page.get_by_text("что такое Юрта").click()
        page.get_by_role("heading", name="Описание МЛК Юрта").click()

    def popup_warning(self, page):
        page.get_by_text("Заполните это поле.")

    def full_check_registration_form(self, page):
        page.locator(config.locators.REGISTRATION_LAST_NAME).fill("buba")
        page.locator(config.locators.REGISTRATION_FIRST_NAME).fill("buba")
        page.locator(config.locators.REGISTRATION_OTCHSTVO).fill("buba")
        page.locator(config.locators.REGISTRATION_PHONE_NUMBER).fill("89275643849")
        page.locator(config.locators.REGISTRATION_EMAIL).fill("salut2005@buba.ru")
        page.locator(config.locators.REGISTRATION_PASSWORD).fill("12345678")
        page.locator(config.locators.REGISTRATION_PASSWORD_SECOND).fill("12345678")
        page.locator("label").filter(has_text="Я принимаю пользовательское соглашение и условия оферты").locator("span").first.click()
        page.locator("label").filter(has_text="Подтверждаю, что я собственник или уполномоченный представитель").locator("span").first.click()
        page.get_by_role("button", name="Зарегистрироваться").click()
        page.get_by_text("Только кириллица. Не более двух слов через пробел или дефис")


