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

    # name = fields.Char(string='')


    def set_open(self):
        for gambar in self:
            pict = self.env['ir.attachment'].sudo().search([('res_model','=', gambar._name),('res_id','=', gambar.id)])

            print(pict)
            return pict
    
    
        

    
    

    