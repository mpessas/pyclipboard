#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pyclipboard import PyClipboard


class TestPyClipboard(unittest.TestCase):

    def setUp(self):
        self.klipper = PyClipboard()

    def test_set_contents(self):
        value = u'test value'
        self.klipper.set_content(value)
        val = self.klipper.get_content()
        self.assertEqual(value, val)

    def test_set_contents_unicode(self):
        value = u'δοκιμαστική τιμή'
        self.klipper.set_content(value)
        val = self.klipper.get_content()
        self.assertEqual(value, val)


if __name__ == '__main__':
    unittest.main()
