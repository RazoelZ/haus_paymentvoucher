from odoo import api, fields, models, _
from email.policy import default
from datetime import datetime
from odoo.exceptions import ValidationError


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
    approved_status = fields.Selection(
        [('waiting', 'Waiting'),
         ('ASM', 'Appilcation Support Manager'),
         ('FD', 'Financial Dept'),
         ('notapprove', 'Not Approved')], string="Status", default="waiting")

    @ api.constrains('date', 'due_date')
    def _check_end_date_greater_than_start_date(self):
        for record in self:
            if record.due_date < record.date:
                raise ValidationError(
                    "Due Date cannot be earlier than Current Date!")

    # Field Bawah
    name = fields.Char(String="Name")
    deptcode = fields.Char(String="Dept. Code")
    amount = fields.Char(String="Amount")
    amount_alphabet = fields.Char(String="Amount Alphabet")
    purpose = fields.Char(String="Purpose")
    requested = fields.Char(String="Requested")
    payment = fields.Selection([
        ('pettycash', 'PETTY CASH'),
        ('advance', 'ADVANCE'),
        ('reimbursment', 'REIMBURSMENT'),
        ('vendor', 'VENDOR'),
        ('pajak', 'PAJAK')
    ], string="Payment")

    # Field untuk pembayaran
    payment_for = fields.Char(String="Payment For")
    receipt_no = fields.Char(String="Receipt No")
    receipt = fields.Selection([
        ('kwitansi', 'NO. KWITANSI'),
        ('invoice', 'NO. INVOICE'),
        ('deliveryorder', 'NO. DELIVERY ORDER'),
        ('goodreceiptnotes', 'NO. GOOD RECEIPT NOTES'),
        ('fakturpajak', 'NO. FAKTUR PAJAK'),
        ('purchaseorder', 'NO. PURCHASE ORDER')
    ], string="Receipt")

    # Field sign writing
    sign_apm = fields.Binary(string="SIGN APPLICATION SUPPORT MANAGER")
    sign_fd = fields.Binary(string="SIGN FINANCIAL DEPT")
