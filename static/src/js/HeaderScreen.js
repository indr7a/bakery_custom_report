/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { Component } from "@odoo/owl";

export class ReceiptHeader extends Component {
    static template = "bakery_custom_report.ReceiptHeader";
    static props = {
        data: {
            type: Object,
            shape: {
                company: Object,
                header: { type: [String, { value: false }], optional: true },
                cashier: { type: String, optional: true },
                "*": true,
            },
        },
    };

    setup() {
        super.setup?.();
        const now = new Date();
        // Format date as dd-mm-yy
        const dd = String(now.getDate()).padStart(2, '0');
        const mm = String(now.getMonth() + 1).padStart(2, '0');
        const yy = String(now.getFullYear()).slice(-2);
        this.props.data.formattedDate = `${dd}-${mm}-${yy}`;
        // Format time as HH:MM
        this.props.data.formattedTime = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    get vatText() {
        if (this.props.data.company.country_id?.vat_label) {
            return _t("%(vatLabel)s: %(vatId)s", {
                vatLabel: this.props.data.company.country_id.vat_label,
                vatId: this.props.data.company.vat,
            });
        }
        return _t("Tax ID: %(vatId)s", { vatId: this.props.data.company.vat });
    }
}
