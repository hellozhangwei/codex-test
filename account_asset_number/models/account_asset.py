from odoo import fields, models


class AccountAsset(models.Model):
    _inherit = "account.asset"

    number = fields.Char(
        string="Number",
        copy=False,
        index=True,
        help="Unique asset number.",
    )

    _sql_constraints = [
        (
            "account_asset_number_unique",
            "unique(number)",
            "Asset number must be unique.",
        )
    ]
