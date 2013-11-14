# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import mock
import os
import sys

from rcfile import rcfile

if sys.version_info[0] == 2:
    configparser = 'ConfigParser.ConfigParser'
else:
    configparser = 'configparser.ConfigParser'


class Testrcfile(unittest.TestCase):

    @mock.patch(configparser)
    def test_rcfile(self, mock_configparser):
        pre_args = {}

        os.environ = {'TEST_RCFILE_A': 1}

        args = rcfile(__name__, pre_args)

        self.assertEqual(args['a'], 1)

        config = mock.Mock()
        config.has_section.return_value = True
        config.items.return_value = [('a', 2)]
        mock_configparser.return_value = config

        args = rcfile(__name__, pre_args)

        self.assertEqual(len(config.read.call_args_list[0][0][0]), 8)
        self.assertTrue('.test_rcfilerc' in config.read.call_args_list[0][0][0])

        self.assertEqual(args['a'], 2)

        pre_args = {'a': 3, 'config': 'abc'}

        args = rcfile(__name__, pre_args)

        self.assertEqual(args['a'], 3)

        self.assertTrue('abc' in config.read.call_args_list[1][0][0])

if __name__ == '__main__':
    unittest.main()
