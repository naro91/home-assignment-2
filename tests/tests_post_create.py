# coding: utf-8
__author__ = 'Abovyan'

import os
import unittest
from pages.page_components import PageObject


class PostCreateTestCase(unittest.TestCase):
    TITLE_CAPACITY = 250
    TEST_LINK = 'https://tech-mail.ru'
    IMG_LINK = 'http://d.topic.lt/FF/images/26/upload/post/201312/13/1232679/9c1834c2e11a68f62a840310457b6316.jpg'
    TITLE_TEXT = 'Wonderful topic'
    MAIN_TEXT = 'This is main text'
    IMG_PATH = os.path.dirname(__file__) + '/images/test_img.jpg'

    def setUp(self):
        self.topic_page_object = PageObject()
        self.topic_page_object.sign_in('ftest6@tech-mail.ru')
        self.topic_page_object.open_page_topic_create()

    def tearDown(self):
        self.topic_page_object.remove_topic()
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
        self.topic_page_object.set_main_text('<strong>' + self.MAIN_TEXT + '</strong>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_bold_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_italic(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<em>' + self.MAIN_TEXT + '</em>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_italic_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_strikethrough_text(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<s>' + self.MAIN_TEXT+ '</s>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_strikethrough_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_underline_text(self):
        self.topic_page_object.select_blog_by_id(2)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<u>' + self.MAIN_TEXT + '</u>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_underline_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_with_img(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.MAIN_TEXT)
        self.topic_page_object.set_main_text('<img src="{}" align="" title="affvf" />'.format(self.IMG_LINK))
        self.topic_page_object.create_topic()
        link = self.topic_page_object.get_img_link()
        self.assertEqual(link, self.IMG_LINK)

    def test_create_blockquote(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<blockquote>' + self.MAIN_TEXT + '</blockquote>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_blockquote_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_blockquote(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<code>' + self.MAIN_TEXT + '</code>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_code_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_ul(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<ul>\n\t<li>' + self.MAIN_TEXT + '</li>\n</ul>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_ul_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_ol(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<ol>\n\t<li>' + self.MAIN_TEXT + '</li>\n</ol>')
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
        self.topic_page_object.set_main_text('<h4>' + self.MAIN_TEXT + '</h4>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_h4_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_h5(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<h5>' + self.MAIN_TEXT + '</h5>')
        self.topic_page_object.create_topic()
        text = self.topic_page_object.get_h5_text()
        self.assertEqual(text, self.MAIN_TEXT)

    def test_create_h6(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text('<h6>' + self.MAIN_TEXT + '</h6>')
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
    # def test_upload_image(self):
    #     self.topic_page_object.select_blog_by_id(34)
    #     self.topic_page_object.load_image(self.IMG_PATH)
    #     self.topic_page_object.set_title(self.TITLE_TEXT)
    #     self.topic_page_object.create_topic()
    #     text = self.topic_page_object.get_editor_text()
    #     self.assertIn('.jpg', text)
