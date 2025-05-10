# from odoo import models

# class PosOrder(models.Model):
#     _inherit = 'pos.order'

#     def print_custom_receipt(self):
#         report = self.env.ref('bakery_custom_report.custom_pos_receipt_report').report_action(self)
#         return {'report_url': report['report_name']}