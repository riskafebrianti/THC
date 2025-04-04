from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta
from odoo.tools import add, float_compare, frozendict, split_every, format_date
from num2words import num2words

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    PO = fields.Char(string='No. PO')


class Accmove(models.Model):
    _inherit = 'account.move'

    def number_to_words(self, amount, currency):

        if currency.name == 'IDR':
            number2words = num2words(amount, lang='id')
            check_number2words = number2words.replace(' koma nol', '')
            amount_to_words = check_number2words.title()+' Rupiah'
        else:
            amount_decimal_check = amount - int(amount)

            if amount_decimal_check == 0.00:
                number2words = num2words(amount, lang='en').title()
            else:
                amount_decimal = '%.2f' % amount
                
                x = amount_decimal.rfind('.')
                amount_before_comma = amount_decimal[:x]
                amount_after_comma = amount_decimal[x+1:]

                number2words1 = num2words(int(amount_before_comma), lang='en').title()
                number2words2 = num2words(int(amount_after_comma), lang='en').title()

                number2words = number2words1+' Point '+number2words2

            if currency.name == 'USD':
                amount_to_words = 'United State Dollar '+number2words
            else:
                amount_to_words = currency.name+' '+number2words

        return amount_to_words
    
class res_partner(models.Model):
    _inherit = 'res.partner'

    badan_hukum = fields.Selection(
        string='tes', store=True,
        selection=[('PT', 'PT'), ('UD', 'UD'), ('CV', 'CV'), ('KOPRASI', 'KOPRASI'), ('YAYASAN', 'YAYASAN')]
    )


class saleOrder(models.Model):
    _inherit = 'sale.order.line'

    keterangan = fields.Char(string='Keterangan')


class ModuleName(models.Model):
    _inherit = 'sale.order'

   
    diskon = fields.Float(string='Diskon Total')

    # def button_dummy(self):

    #     self.supply_rate()
    #     return True

    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total','diskon')
    def _compute_amounts(self):
        """Compute the total amounts of the SO."""
        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)

            if order.company_id.tax_calculation_rounding_method == 'round_globally':
                tax_results = self.env['account.tax']._compute_taxes([
                    line._convert_to_tax_base_line_dict()
                    for line in order_lines
                ])
                totals = tax_results['totals']
                amount_untaxed = totals.get(order.currency_id, {}).get('amount_untaxed', 0.0)
                amount_tax = totals.get(order.currency_id, {}).get('amount_tax', 0.0)
                diskon = totals.get(order.currency_id, {}).get('diskon', 0.0)
            else:
                amount_untaxed = sum(order_lines.mapped('price_subtotal'))
                amount_tax = sum(order_lines.mapped('price_tax'))
                diskon = self.diskon

            order.amount_untaxed = amount_untaxed
            order.amount_tax = amount_tax
            order.diskon = diskon
            order.amount_total = order.amount_untaxed + order.amount_tax - order.diskon

    
    # @api.depends('amount_untaxed', 'amount_tax', 'diskon')
    # def _compute_amount(self):
    #     for order in self:
    #         super(saleOrder, order)._compute_amount()
    #         order.amount_total -= order.diskon
    # @api.onchange('diskon')
    # def _onchange_diskon(self):
    #     if self.diskon:
    #         self.amount_untaxed = self.amount_undiscounted - self.diskon  # ✅ Perbaikan: Tetapkan langsung
    #         print(self)
    
    def set_open(self):
        for gambar in self:
            pict = self.env['ir.attachment'].sudo().search([('res_model','=', gambar._name),('res_id','=', gambar.id)])

            print(pict)
            return pict
    
    
        

    
    

    