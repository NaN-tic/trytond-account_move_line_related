#!/usr/bin/env python
# This file is part of account_move_line_related module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class AccountMoveLineRelatedTestCase(unittest.TestCase):
    '''Test Account Move Line Related module'''

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_move_line_related')

    def test0006depends(self):
        '''Test depends'''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountMoveLineRelatedTestCase))
    return suite
