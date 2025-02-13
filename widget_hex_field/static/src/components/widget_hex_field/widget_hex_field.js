/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useInputField } from "@web/views/fields/input_field_hook";
import { useRef, Component, onWillPatch } from "@odoo/owl";


class HexField extends Component {
    static template = 'widget_hex_field.HexField';
    static props = {
        ...standardFieldProps,
        value: { type: String, optional: true },
        delimiter: { type: String, optional: true },
        minPairs: { type: Number, optional: true },
        maxPairs: { type: Number, optional: true },
        placeholder: { type: String, optional: true },
    };
    static defaultProps = {
        delimiter: '-',
        minPairs: 3,
        maxPairs: 6,
    };

    setup() {
        this.input = useRef("input");
        useInputField({
            getValue: () => this.props.record.data[this.props.name] || "",
            parse: (v) => this.parse(v),
        });

        onWillPatch(() => {
            this.props.value = this.props.record.data[this.props.name];
            const regex = new RegExp(`^[0-9A-Fa-f]{2}(${this.props.delimiter}[0-9A-Fa-f]{2}){${this.props.minPairs - 1},${this.props.maxPairs - 1}}$`);
            if (!regex.test(this.props.value)) {
                this.props.record.setInvalidField(this.props.name);
            }
        });
    }

    parse(value) {
        let res = value.trim();
        res = res.toUpperCase();
        return res;
    }

}

export const hexField = {
    component: HexField,
    displayName: _t('Hex Field'),
    supportedFieldTypes: ['char'],
    extractProps: ({ attrs, options }) => ({
        delimiter: options.delimiter || '-',
        // minPairs should adjust in case is 0, less or undefined
        minPairs: options.minPairs || 3,
        maxPairs: options.maxPairs || 6,
        placeholder: attrs.placeholder,
    }),
}

registry.category('fields').add('hex', hexField);
