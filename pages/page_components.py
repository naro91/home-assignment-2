# coding: utf-8
__author__ = 'Abovyan'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import os

class PageObject():
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'
    CREATING_TOPIC = '//h2[@class="page-header"]'
    CREATE_BUTTON_XPATH = '//button[contains(text(),"Создать")]'
    MAIN_TEXT = '#id_text'

    def __init__(self):
        self.driver = webdriver.Remote(
           command_executor='http://127.0.0.1:5555/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, os.environ.get('TTHA2BROWSER', 'CHROME'))
        )
        self.driver.get('http://ftest.stud.tech-mail.ru/')

    def click_button_login(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def sign_in(self, login):
        self.click_button_login()
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(os.environ.get('TTHA2PASSWORD'))
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
        return user.is_displayed()

    def close(self):
        self.driver.quit()

    def click_create_topic(self):
        self.driver.find_element_by_id('modal_write_show').click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.write-item-type-topic>.write-item-link'))
        ).click();

    def is_page_creating_topic(self):
        wait = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CREATING_TOPIC))
        )
        text_field = wait.text
        return (wait.is_displayed() and (text_field == u'Создание топика') )

    def select_blog_by_id(self, num):
        select = self.driver.find_element_by_css_selector('#id_blog_chzn>.chzn-single')
        select.click()
        option = self.driver.find_element_by_css_selector('#id_blog_chzn .active-result:nth-child({})'.format(num))
        option.click()

    def open_page_topic_create(self):
        self.driver.get('http://ftest.stud.tech-mail.ru/blog/topic/create/')

    def set_title(self, title):
        field = self.driver.find_element_by_id('id_title')
        field.send_keys(title)


    def set_main_text(self, text):
        field = self.driver.find_element_by_css_selector(self.MAIN_TEXT)
        ActionChains(self.driver).click(field).send_keys(text).perform()

    def create_topic(self):
        self.driver.find_element_by_css_selector('button.button:nth-child(14)').submit()
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON_XPATH))).submit()


    def get_content(self):
        content = self.driver.find_element_by_css_selector('.topic-content')
        return content.text

    def remove_topic(self):
        remove_link = self.driver.find_element_by_css_selector('.actions-delete')
        remove_link.click()
        remove_form = self.driver.find_element_by_css_selector('input.button')
        remove_form.submit()

    def get_title(self):
        title = self.driver.find_element_by_css_selector('h1.topic-title>a')
        return title.text

    def add_questionnaire(self, question, answers):
        poll_checkbox = self.driver.find_element_by_css_selector('#container [name="add_poll"]')
        poll_checkbox.click()
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_question"]')))
        elem.send_keys(question)
        for i,temp in enumerate(answers):
            self.driver.find_element_by_id('id_form-{}-answer'.format(i)).send_keys(temp)


    def find_questionnaire(self):
        ans1 = self.driver.find_element_by_xpath('.//ul[@class="poll-vote"]/li[1]/label').text
        ans2 = self.driver.find_element_by_xpath('.//ul[@class="poll-vote"]/li[2]/label').text
        return {ans1, ans2}

    def get_bold_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > strong:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_italic_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > em:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_strikethrough_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > s:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_underline_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > u:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_img_link(self):
        try:
            url = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]//img').get_attribute('src')
        except NoSuchElementException:
            return None
        return url

    def get_blockquote_text(self):
        try:
            url = self.driver.find_element_by_css_selector('.topic-content > blockquote:nth-child(1)').text
        except NoSuchElementException:
            return None
        return url

    def get_code_text(self):
        try:
            url = self.driver.find_element_by_css_selector('.topic-content > code:nth-child(1)').text
        except NoSuchElementException:
            return None
        return url

    def get_ul_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > ul:nth-child(1) > li:nth-child(2)').text
        except NoSuchElementException:
            return None
        return text

    def get_ol_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > ol:nth-child(1) > li:nth-child(2)').text
        except NoSuchElementException:
            return None
        return text

    def get_link_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > a:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_link(self):
        try:
            link = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]//a').get_attribute('href')
        except NoSuchElementException:
            return None
        return link

    def get_h4_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > h4:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_h5_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > h5:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_h6_text(self):
        try:
            text = self.driver.find_element_by_css_selector('.topic-content > h6:nth-child(1)').text
        except NoSuchElementException:
            return None
        return text

    def get_add_comment(self):
        try:
            temp = self.driver.find_element_by_css_selector('.comment-add-link').is_displayed()
        except NoSuchElementException:
            return False
        return temp

    def set_forbid_comment(self):
        poll_checkbox = self.driver.find_element_by_css_selector('#id_forbid_comment')
        poll_checkbox.click()

    def has_error_on_page(self):
        error = self.driver.find_element_by_class_name('system-message-error')
        return error.is_displayed()

    def open_form_for_load_img(self):
        self.driver.find_element_by_css_selector('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(15)').click()

    def load_image(self, path):
        # self.driver.find_element_by_css_selector('#id_text').send_keys('Test text')
        self.driver.find_element_by_css_selector('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(15)').click()
        element = self.driver.find_element_by_css_selector('#img_file')
        ActionChains(self.driver).send_keys_to_element(element, path).perform()
        # self.driver.find_element_by_css_selector('#img_file').send_keys(path)
        self.driver.find_element_by_css_selector('#submit-image-upload').click()


    def get_editor_text(self):
        return self.driver.find_element_by_css_selector('.topic-content > img:nth-child(1)').get_attribute('src')
