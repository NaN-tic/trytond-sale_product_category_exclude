# This file is part of the sale_product_category_exclude module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'
    avoid_products = fields.Function(fields.One2Many(
            'product.product', None, 'Product Category Domain'),
        'get_avoid_products')

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        cls._error_messages.update({
                'unsalable_product': 'The product "%s" is not salable for '
                    'the party "%s".',
                })

    def get_avoid_products(self, lines=None):
        pool = Pool()
        ProductCategory = pool.get('party.party-product.category')
        Template = pool.get('product.template')
        party = self.sale.party
        product_categories = ProductCategory.search([('party', '=', party)])
        products = []
        for product_category in product_categories:
            templates = Template.search([
                    ('category', '=', product_category.category)])
            for template in templates:
                for product in template.products:
                    products.append(product.id)
        return products

    @classmethod
    def validate(cls, lines):
        super(SaleLine, cls).validate(lines)
        for line in lines:
            if line.product in line.avoid_products:
                cls.raise_user_error('unsalable_product',
                    (line.product.rec_name, line.sale.party.rec_name))
