var signature_pads = {};
    Vue.component('signaturepad', {
        template:
            `<canvas  v-bind:id="ln_props.id" :class="ln_props.classes"  :style="ln_props.style" :width="ln_props.width" height="ln_props.height"></canvas>`,
        methods: {
            pad_change() {
                var id = this.$props.ln_props.id.toString();
                var canvas = document.getElementById(id);
                var signaturePad = new SignaturePad(canvas, this.$props.ln_props.options);
                signature_pads[id] = signaturePad;
                var events = this.$props.ln_props.events;
                var props = this.$props;

                function onEnd() {
                    if (events.includes('onEnd')) {
                        var data = signaturePad.toDataURL('image/png');
                        var point_data = signaturePad.toData();
                        var e = {
                            'event_type': 'onEnd',
                            'id': props.ln_props.id,
                            'class_name': props.ln_props.class_name,
                            'html_tag': props.ln_props.html_tag,
                            'vue_type': props.ln_props.vue_type,
                            'page_id': page_id,
                            'websocket_id': websocket_id,
                            'data': data,
                            'point_data': point_data
                        };
                        send_to_server(e, 'event');
                    }
                }

                signaturePad.onEnd = onEnd;

            }
        },
        mounted() {
            this.pad_change();
        },
        updated() {

            if (this.$props.ln_props.clear) {
                signature_pads[this.$props.ln_props.id.toString()].clear();
            }
        },
        props: {
            ln_props: Object
        }
    });