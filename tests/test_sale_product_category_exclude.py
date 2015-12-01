# This file is part of the sale_product_category_exclude module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleProductCategoryExcludeTestCase(ModuleTestCase):
    'Test Sale Product Category Exclude module'
    module = 'sale_product_category_exclude'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleProductCategoryExcludeTestCase))
    return suite