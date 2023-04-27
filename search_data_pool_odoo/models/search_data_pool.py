from odoo import models, fields, api

class SearchDataPool(models.TransientModel):
    _name = 'search.data.pool'
    _description = 'Search Data Pool Wizard'

    search_keyword = fields.Char(string='Keyword')

    def search_products(self):
        # Implement the search logic here
        pass
