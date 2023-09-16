{
    'name': 'Clear Website Cart',
    'description': 'Clear website cart',
    "author": "Cybrosys",
    "depends": [
        "base",
        'sale',
        'website',
        'website_sale',
    ],
    "data": [
        'views/website_sale_view.xml',
    ],
    'assets': {
        'web.assets_frontend':
            ['clear_cart_website/static/src/js/clear_cart.js']

    },
    "application": True,
    'installable': True,

}
