#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    """测试name_function.py"""
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', 'amanda', )
        self.assertEqual(formatted_name, 'Janis Amanda Joplin')


if __name__ == '__main__':
    unittest.main()
