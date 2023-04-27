from odoo import models, fields, api

class SearchDataPool(models.TransientModel):
    _name = 'search.data.pool'
    _description = 'Search Data Pool Wizard'

    search_keyword = fields.Char(string='Keyword')
    search_result_ids = fields.One2many('search.data.pool.result', 'search_id', string='Search Results')

    def search_products(self):
        # Implement the search logic here using REST API
        # For demonstration purposes, we will create dummy data
        search_results = [
            {
                'article_number': '123',
                'title': 'Product 1',
                'manufacturer': 'Manufacturer 1',
                'price': 100.0,
            },
            {
                'article_number': '456',
                'title': 'Product 2',
                'manufacturer': 'Manufacturer 2',
                'price': 200.0,
            },
        ]

        search_result_lines = []
        for result in search_results:
            search_result_lines.append((0, 0, result))
        self.search_result_ids = search_result_lines

class SearchDataPoolResult(models.TransientModel):
    _name = 'search.data.pool.result'
    _description = 'Search Data Pool Result Line'

    search_id = fields.Many2one('search.data.pool', ondelete='cascade')
    article_number = fields.Char(string='Article Number')
    title = fields.Char(string='Title')
    manufacturer = fields.Char(string='Manufacturer')
    price = fields.Float(string='Price')
    add_to_catalog = fields.Boolean(string='Add to Catalog')

    def add_products_to_catalog(self):
        for line in self.search_id.search_result_ids:
            if line.add_to_catalog:
                self.env['product.product'].create({
                    'name': line.title,
                    'default_code': line.article_number,
                    'manufacturer': line.manufacturer,
                    'list_price': line.price,
                })
