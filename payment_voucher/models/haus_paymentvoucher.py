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
    due_date = fields.Date(String="Due Date", required=True)
    bankacc = fields.Char(String="Bank Account")
    bankacc_holder = fields.Char(String="Bank Account Holder")
    bank_name = fields.Char(String="Bank Name")
    approved_status = fields.Selection(
        [('waiting', 'Waiting'),
         ('ASM', 'Appilcation Support Manager'),
         ('FD', 'Financial Dept'),
         ('done', 'Done'),
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

    # purpose = fields.Char(String="Purpose")
    requested = fields.Char(String="Requested")
    payment = fields.Selection([
        ('pettycash', 'PETTY CASH'),
        ('advance', 'ADVANCE'),
        ('reimbursment', 'REIMBURSMENT'),
        ('vendor', 'VENDOR'),
        ('pajak', 'PAJAK')
    ], string="Payment")

    # Field untuk pembayaran
    payment_for = fields.Char(String="PAYMENT FOR")
    receipt_no = fields.Char(String="NO. KWITANSI")
    invoice_no = fields.Char(String="NO INVOICE")
    delivery_order_no = fields.Char(String="NO. DELIVERY ORDER")
    good_receipt_notes_no = fields.Char(String="NO. GOOD RECEIPT NOTES")
    tax_invoice_no = fields.Char(String="NO. FAKTUR PAJAK")
    purchase_order_no = fields.Char(String="NO. PURCHASE ORDER")

    fields.Selection([
        ('kwitansi', 'NO. KWITANSI'),
        ('invoice', 'NO. INVOICE'),
        ('deliveryorder', 'NO. DELIVERY ORDER'),
        ('goodreceiptnotes', 'NO. GOOD RECEIPT NOTES'),
        ('fakturpajak', 'NO. FAKTUR PAJAK'),
        ('purchaseorder', 'NO. PURCHASE ORDER')
    ], string="Receipt")

    # Signature Field
    requested_signature = fields.Binary(
        string='Requested Signature', widget='sign')
    requested_name = fields.Char(String="Requested By")
    approved_signature = fields.Binary(
        string='Approved Signature', widget='sign')
    approved_name = fields.Char(String="Approveed By")
    paid_signature = fields.Binary(string='Paid Signature', widget='sign')
    paid_name = fields.Char(String="Paid By")
    received_signature = fields.Binary(
        string='Received Signature', widget='sign')
    received_name = fields.Char(String="Received By")

    @api.onchange('requested_signature', 'requested_name')
    def change_to_apm(self):
        if self.requested_signature and self.requested_name:
            self.approved_status = 'ASM'

    @api.onchange('approved_signature', 'approved_name', 'requested_signature', 'requested_name')
    def change_to_fd(self):
        if self.approved_signature and self.approved_name and self.requested_signature and self.requested_name:
            self.approved_status = 'FD'

    @api.onchange('paid_signature', 'paid_name', 'approved_signature', 'approved_name', 'requested_signature', 'requested_name', 'received_signature', 'received_name')
    def change_to_done(self):
        if self.paid_signature and self.paid_name and self.approved_signature and self.approved_name and self.requested_signature and self.requested_name and self.received_signature and self.received_name:
            self.approved_status = 'done'

    def not_approved(self):
        self.approved_status = 'notapprove'
