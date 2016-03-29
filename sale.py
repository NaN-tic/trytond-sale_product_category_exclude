# This file is part of the sale_product_category_exclude module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['SaleLine']


class SaleLine:
    __metaclass__ = PoolMeta
    __name__ = 'sale.line'

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        cls._error_messages.update({
                'unsalable_product': 'The product "%s" is not salable for '
                    'the party "%s".',
                })

    @classmethod
    def validate(cls, lines):
        pool = Pool()
        PartyProductCategory = pool.get('party.party-product.category')

        super(SaleLine, cls).validate(lines)
        for line in lines:
            party = line.sale.party
            party_product_categories = PartyProductCategory.search(
                [('party', '=', party)])
            product_categories = [ppc.category for ppc in
                party_product_categories]
            if (line.product and line.product.template.category and
                    line.product.template.category in product_categories):
                cls.raise_user_error('unsalable_product',
                    (line.product.rec_name, line.sale.party.rec_name))
