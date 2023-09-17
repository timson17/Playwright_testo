from playwright.sync_api import Page
import config


class IndexPage:
    LOGIN_INPUT = "//input[@id='login']"
    PASSWORD_INPUT = "//input[@id='password']"
    ENTRY_BUTTON = "//button[@type='submit']"
    NOTICE_BAD_DATA = "//div[@class='notice__descr']"
    SERVICE_PROVIDER_LINK = "//a[contains(text(),'Поставщикам услуг')]"
    REGISTRATION_BUTTON = "//button[@type='button']"
    REGISTRATION_FORM_CHECK = "//label[@for='registration-surname']"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def insert_login(self, page: Page) -> None:
        page.locator(self.LOGIN_INPUT).fill("89373176733")

    def insert_password(self, page: Page) -> None:
        page.locator(self.PASSWORD_INPUT).fill("12345678")

    def button_click(self, page: Page) -> None:
        page.locator(self.ENTRY_BUTTON).click()

    def check_by_title(self,page: Page) -> None:
        return page.title()

    def insert_incorrect_login(self, page: Page) -> None:
        page.locator(self.LOGIN_INPUT).fill("32748932489")

    def insert_incorrect_password(self, page: Page) -> None:
        page.locator(self.PASSWORD_INPUT).fill("3724672384")

    def check_notice_uncorrect_data(self, page: Page) -> None:
        return page.locator(self.NOTICE_BAD_DATA).inner_text()

    def link_service_provider_click(self, page: Page) -> None:
        page.locator(self.SERVICE_PROVIDER_LINK).click()

    def reg_button_click(self, page: Page) -> None:
        page.locator(self.REGISTRATION_BUTTON).click()

    def check_registration_form(self, page: Page) -> None:
        return page.locator(self.REGISTRATION_FORM_CHECK).inner_text()