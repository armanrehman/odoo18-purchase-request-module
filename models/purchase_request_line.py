from odoo import models, fields

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'
    _order = 'sequence, id'

    request_id = fields.Many2one('purchase.request', string='Purchase Request', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    item_description = fields.Char(string='Item Description')
    vendor_id = fields.Many2one('res.partner', string='Vendor', domain=[('supplier_rank', '>', 0)])
    required_date = fields.Date(string='Required Date')
    required_qty = fields.Float(string='Required Qty')
    info_price = fields.Float(string='Info Price')
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure')