import allure
from selene import browser, have


class Github:
    @allure.step("Открываем github")
    def open_github(self):
        browser.open("https://github.com")

    @allure.step('ищем свой репозиторий')
    def search_repository(self):
        browser.element("[data-target='qbsearch-input.inputButton']").click()
        browser.element("#query-builder-test").type('nlevusenkov/qa_guru_homework5').press_enter()

    @allure.step("Переходим в свой репозиторий")
    def go_to_repository(self):
        browser.element("[href='/nlevusenkov/qa_guru_homework5']").click()

    @allure.step("Переходим во вкладку issue")
    def open_issue(self):
        browser.element('#issues-tab').click()

    @allure.step("Проверяем имя issue")
    def find_issue_name(self, value):
        browser.element('[data-testid="issue-pr-title-link"]').should(have.text(value))

    # через with
    def open_github2(self):
        with allure.step('Открываем github'):
            browser.open("https://github.com")

    def search_repository2(self):
        with allure.step('ищем свой репозиторий'):
            browser.element("[data-target='qbsearch-input.inputButton']").click()
            browser.element("#query-builder-test").type('nlevusenkov/qa_guru_homework5').press_enter()

    def go_to_repository2(self):
        with allure.step('Переходим в свой репозиторий'):
            browser.element("[href='/nlevusenkov/qa_guru_homework5']").click()

    def open_issue2(self):
        with allure.step('Переходим во вкладку issue'):
            browser.element('#issues-tab').click()

    def find_issue_name(self, value):
        with allure.step('Проверяем имя issue'):
            browser.element('[data-testid="issue-pr-title-link"]').should(have.text(value))