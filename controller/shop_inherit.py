# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '/shop',
        '/shop/cart',
    ], type='json', auth="public", website=True, )
    def shop(self, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None,
                                                   search='', min_price=0.0,
                                                   max_price=0.0, ppg=False,
                                                   **post)
        cart_quantity = len(request.website.sale_get_order().order_line)
        res.qcontext[
            'cart_quantity'] = cart_quantity
        return res
