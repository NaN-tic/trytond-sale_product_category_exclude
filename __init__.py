# This file is part of the sale_product_category_exclude module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .party import *
from .sale import *


def register():
    Pool.register(
        PartyProductCategory,
        Party,
        SaleLine,
        module='sale_product_category_exclude', type_='model')
