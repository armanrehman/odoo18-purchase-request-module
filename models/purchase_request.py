from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'
    _order = 'id desc'

    name = fields.Char(string='Request Number', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    requester_id = fields.Many2one('res.users', string='Requester', required=True, default=lambda self: self.env.user)
    branch = fields.Char(string='Branch')
    department = fields.Char(string='Department')
    posting_date = fields.Date(string='Posting Date', default=fields.Date.context_today)
    valid_until = fields.Date(string='Valid Until')
    document_date = fields.Date(string='Document Date', default=fields.Date.context_today)
    required_date = fields.Date(string='Required Date')
    line_ids = fields.One2many('purchase.request.line', 'request_id', string='Request Lines')
    purchase_order_id = fields.Many2one('purchase.order', string='Related Purchase Order')
    state = fields.Selection([
        ('rfq', 'RFQ'),
        ('rfq_sent', 'RFQ Sent'),
        ('purchase_order', 'Purchase Order'),
    ], string='Status', default='rfq', tracking=True)

    def action_confirm_requisition(self):
        for rec in self:
            rec.state = 'rfq_sent'

    def action_print_requisition(self):
        return self.env.ref('purchase_request.action_report_purchase_request').report_action(self)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or _('New')
        return super().create(vals)