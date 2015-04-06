# coding: utf-8
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Abovyan'

import os
import unittest
from pages.page_components import PageObject


class PostCreateTestCase(unittest.TestCase):
    TITLE_CAPACITY = 250
    TEST_LINK = 'https://tech-mail.ru'
    IMG_LINK = 'd.topic.lt/FF/images/26/upload/post/201312/13/1232679/9c1834c2e11a68f62a840310457b6316.jpg'
    TITLE_TEXT = 'Wonderful topic'
    MAIN_TEXT = 'This is main text'
    IMG_PATH = os.path.dirname(__file__) + '/images/test_img.jpg'

    def setUp(self):
        self.topic_page_object = PageObject()
        self.topic_page_object.sign_in('ftest6@tech-mail.ru')
        self.topic_page_object.open_page_topic_create()

    def tearDown(self):
        try:
            self.topic_page_object.remove_topic()
        except NoSuchElementException:
            pass
        self.topic_page_object.close()

    def test_create_topic(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertEqual(self.topic_page_object.get_content(), self.MAIN_TEXT)

    def test_title_capacity(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title('a' * self.TITLE_CAPACITY)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertEqual(self.topic_page_object.get_title(), 'a' * self.TITLE_CAPACITY)

    def test_create_topic_with_questionnaire(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        question = 'How Many Stars Are There in the Sky?'
        answers = {u"I dont know", u"maybe 1000000000"}
        self.topic_page_object.add_questionnaire(question, answers)
        self.topic_page_object.create_topic()
        return_answers = self.topic_page_object.find_questionnaire()
        self.assertEqual(return_answers, answers)



    def test_create_bold(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_bold_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_italic(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_italic_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_strikethrough_text(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(7)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_strikethrough_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_underline_text(self):
        self.topic_page_object.select_blog_by_id(2)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(8)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_underline_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_with_img(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.MAIN_TEXT)
        self.topic_page_object.click_button('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(15)')
        self.topic_page_object.click_button('li.js-block-upload-img-item:nth-child(2) > a:nth-child(1)')
        self.topic_page_object.set_text('#img_url', self.IMG_LINK)
        self.topic_page_object.click_button('#submit-image-upload-link')
        self.topic_page_object.create_topic()
        link = self.topic_page_object.get_img_link()
        self.assertEqual(link, 'http://{}'.format(self.IMG_LINK))

    def test_create_blockquote(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(9)')
        self.topic_page_object.come_back_and_set_text(13, self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_blockquote_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_blockquote(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(10)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_code_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_ul(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(12)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_ul_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_ol(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(13)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_ol_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_link(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<a href="{}">{}</a>'.format(self.TEST_LINK, self.MAIN_TEXT))
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_link_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_h4(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_h4_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_h5(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_h5_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_h6(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.click_button_and_set_text('#markItUpId_text > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3)')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_h6_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_without_comment(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.set_forbid_comment()
        self.topic_page_object.create_topic()
        add_comment = self.topic_page_object.get_add_comment()
        self.assertFalse(add_comment)

    def test_create_with_user(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text(u'<a href="/profile/m.smirnov/">Михаил Смирнов</a>')
        self.topic_page_object.create_topic()
        href = self.topic_page_object.get_link()
        self.assertIn('/profile/m.smirnov/', href)


    # в режиме дебага (пошаговом проходе) работает а при нормальном запуске нет
    def test_upload_image(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.load_image(self.IMG_PATH)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_editor_text()
        self.assertIn('.jpg', text)
