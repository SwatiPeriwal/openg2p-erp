# -*- coding: utf-8 -*-
from odoo import fields, models, api


class GeneralExportWizard(models.TransientModel):
    _name = "general.export.wizard"
    _description = "Export CSV"

    use_active_domain = fields.Boolean("Use active domain")

    @api.multi
    def action_export(self):
        self.ensure_one()
        report_id = self.env.context.get("redirect_report_id","")
        active_domain = self.env.context.get("active_domain",[])
        active_ids = self.env.context.get("active_ids",[])
        data = {
            "use_active_domain": str(self.use_active_domain).lower(),
            "active_domain": active_domain,
            "active_ids": active_ids,
        }
        return self.env.ref(report_id).report_action([], data=data)