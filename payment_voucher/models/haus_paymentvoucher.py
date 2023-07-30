from odoo import api, fields, models, _
from email.policy import default
from datetime import datetime


class HausPaymentVoucher(models.Model):
    _name = "haus.paymentvoucher"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Haus Payment Voucher Form"

    # Field Atas
    no_voucher = fields.Char(String="No")
    date = fields.Date(String="Date", default=datetime.today())
    due_date = fields.Date(String="Due Date")
    bankacc = fields.Char(String="Bank Account")
    bankacc_holder = fields.Char(String="Bank Account Holder")
    bank_name = fields.Char(String="Bank Name")

    # Field Bawah
    name = fields.Char(String="Name")
    deptcode = fields.Char(String="Dept. Code")
    amount = fields.Char(String="Amount")
    amount_alphabet = fields.Char(String="Amount Alphabet")
    purpose = fields.Char(String="Purpose")
    requested = fields.Char(String="Requested")
    payment = fields.Selection([
        ('pettycash', 'Petty Cash'),
        ('advance', 'Advance'),
        ('reimbursment', 'Reimbursment'),
        ('vendor', 'Vendor'),
        ('pajak', 'Pajak')
    ], string="Payment")

    # Field untuk pembayaran
    payment_for = fields.Char(String="Payment For")
    receipt_no = fields.Char(String="Receipt No")
    receipt = fields.Selection([
        ('kwitansi', 'No. Kwitansi'),
        ('invoice', 'No. Invoice'),
        ('deliveryorder', 'No. Delivery Order'),
        ('goodreceiptnotes', 'No. Good Receipt Notes'),
        ('fakturpajak', 'No. Faktur Pajak'),
        ('purchaseorder', 'No. Purchase Order')
    ], string="Receipt")