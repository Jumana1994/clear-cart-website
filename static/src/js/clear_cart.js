odoo.define('clear_cart_website.clear_cart', function (require) {
   'use strict';

    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');

    publicWidget.registry.clearCartButton = publicWidget.Widget.extend({
        selector: '.clear-cart-button',
        events: {
            'click #clear_cart_button': '_onClickClearCart',
        },
        _onClickClearCart: function (ev) {
            ev.preventDefault();
            var self = this;
            $('#myModal').modal('show');
            $('#myModal').on('click', '.confirm-clear', function () {
                self._clearCart();
            });
        },
        _clearCart: function () {
            var self = this;

            rpc.query({
                route: '/shop/clear_cart',
                params: {},
            }).then(function (result) {
                if (result.success) {
                    location.reload();
                }
            });
        },
        _showModal: function (message) {
            $('#myModal .modal-body p').text(message);
            $('#myModal').modal('show');
        },
    });
    return publicWidget;
});
