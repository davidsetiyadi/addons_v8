# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.http import request
from openerp.addons.ehcs_qr_code_base.models.qr_code_base import generate_qr_code


class QRCodeInvoice(models.Model):
    _inherit = 'account.invoice'

    qr_image = fields.Binary("QR Code", compute='_generate_qr_code')
    qr_in_report = fields.Boolean('Show QR in Report')

    @api.one
    def _generate_qr_code(self):
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        # base_url = 'suksesssss'
        self.qr_image = generate_qr_code(base_url)
