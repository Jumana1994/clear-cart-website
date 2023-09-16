# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteSaleController(http.Controller):

    @http.route('/shop/clear_cart', type='json', auth='user', website=True)
    def clear_cart(self):
        website = request.website
        partner = request.env.user.partner_id
        sale_order = request.env['sale.order'].sudo().search([
            ('state', '=', 'draft'),
            ('partner_id', '=', partner.id),
            ('website_id', '=', website.id)
        ])

        if sale_order and sale_order.website_order_line:
            sale_order.website_order_line.unlink()
            return {
                'success': True,
                'message': 'Cart cleared successfully.',
            }
        else:
            return {
                'success': False,
                'message': 'Failed to clear cart.',
            }
