__author__ = 'Abovyan'

import unittest
from pages.page_components import PageObject


class PostTestCase(unittest.TestCase):
    TITLE_CAPACITY = 250
    TITLE_TEXT = 'Wonderful topic'
    MAIN_TEXT = 'This is main text'

    def setUp(self):
        self.topic_page_object = PageObject()
        self.topic_page_object.sign_in('ftest6@tech-mail.ru')
        self.topic_page_object.open_page_topic_create()

    def tearDown(self):
        self.topic_page_object.close()

    def test_create_without_select_blog(self):
        self.topic_page_object.select_blog_by_id(1)
        self.topic_page_object.set_title(self.TITLE_TEXT)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertTrue(self.topic_page_object.has_error_on_page())

    def test_create_without_set_title(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertTrue(self.topic_page_object.has_error_on_page())


    def test_create_without_text(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertTrue(self.topic_page_object.has_error_on_page())

    def test_create_title_greater_max_long(self):
        self.topic_page_object.select_blog_by_id(34)
        self.topic_page_object.set_title('a' * (self.TITLE_CAPACITY + 1))
        self.topic_page_object.set_main_text(self.MAIN_TEXT)
        self.topic_page_object.create_topic()
        self.assertTrue(self.topic_page_object.has_error_on_page())
