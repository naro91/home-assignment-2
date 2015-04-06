
__author__ = 'Abovyan'

import unittest
from pages.page_components import PageObject


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.page = PageObject()
        self.assertTrue(self.page.sign_in('ftest6@tech-mail.ru'))

    def tearDown(self):
        self.page.close()

    def test_open_creating_topic(self):
        self.page.click_create_topic()
        self.assertTrue(self.page.is_page_creating_topic())