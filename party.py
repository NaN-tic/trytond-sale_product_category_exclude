# This file is part of the sale_product_category_exclude module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['PartyProductCategory', 'Party']
__metaclass__ = PoolMeta


class PartyProductCategory(ModelSQL, ModelView):
    'Party - Product Category'
    __name__ = 'party.party-product.category'
    _table = 'party_party_product_category_rel'
    party = fields.Many2One('party.party', 'Party', select=True, required=True)
    category = fields.Many2One('product.category', 'Category', select=True,
        required=True)


class Party:
    __name__ = 'party.party'
    product_categories = fields.Many2Many('party.party-product.category',
        'party', 'category', 'Product Categories to exclude',
        help="Exclude these categories when products are added in sale lines")
