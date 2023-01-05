# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_done(self):
        if not self.user_has_groups("sale_order_lock_with_access_right.group_sale_order_lock_unlock"):
            raise UserError(_("You have not necessary rights to do this action,please contact the administrator"))
        return super(SaleOrder, self).action_done()

    def action_unlock(self):
        if not self.user_has_groups("sale_order_lock_with_access_right.group_sale_order_lock_unlock"):
            raise UserError(_("You have not necessary rights to do this action,please contact the administrator"))
        return super(SaleOrder, self).action_unlock()