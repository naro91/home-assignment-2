# coding: utf-8
import unittest
import os
import sys

from tests.test_post_with_empty_fields import PostTestCase
from tests.tests_post_create import PostCreateTestCase
from tests.test_sign_in_and_open_c_topic import MainTestCase

source_dir = os.path.join(os.path.dirname(__file__), 'tests')

if __name__ == '__main__':

    if 'TTHA2PASSWORD' not in os.environ:
        sys.exit('No password set')

    suite = unittest.TestSuite((
        unittest.makeSuite(PostTestCase),
        unittest.makeSuite(PostCreateTestCase),
        unittest.makeSuite(MainTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())