var full_calendars = {};
Vue.component('fullcalendar', {
    template:
        `<div  v-bind:id="ln_props.id" :class="ln_props.classes"  :style="ln_props.style" ></div>`,

    methods: {
        get_all_events(calendar) {
            let all_events = [];
            for (let event_obj of calendar.getEvents()) {
                all_events.push(this.create_object_from_event(event_obj))
            }
            return all_events;
        },
        create_object_from_event(event_obj) {
            const event_properties = ['id', 'groupId', 'allDay', 'start', 'end', 'title', 'url', 'classNames',
                'editable', 'startEditable', 'durationEditable', 'resourceEditable', 'rendering', 'overlap',
                'constraint', 'backgroundColor', 'borderColor', 'textColor', 'extendedProps'];
            let event_data = {};
            for (let i of event_properties) {
                event_data[i] =event_obj[i];
            }
            return event_data;
        },
        calendar_change() {
            var id = this.$props.ln_props.id.toString();
            var events = this.$props.ln_props.events;
            var props = this.$props;
            var calendarEl = document.getElementById(id);
            var calendar = new FullCalendar.Calendar(calendarEl, this.$props.ln_props.options);
            const parent_comp = this;
            if (events.includes('eventClick'))
                calendar.on('eventClick', function (info) {
                    var e = {
                        'event_type': 'eventClick',
                        'id': props.ln_props.id,
                        'class_name': props.ln_props.class_name,
                        'html_tag': props.ln_props.html_tag,
                        'vue_type': props.ln_props.vue_type,
                        'page_id': page_id,
                        'websocket_id': websocket_id,
                        'event_data': parent_comp.create_object_from_event(info.event),
                        'all_events': parent_comp.get_all_events(calendar)
                    };
                    send_to_server(e, 'event');
                });

            if (events.includes('eventDrop'))
                calendar.on('eventDrop', function (info) {
                    var e = {
                        'event_type': 'eventDrop',
                        'id': props.ln_props.id,
                        'class_name': props.ln_props.class_name,
                        'html_tag': props.ln_props.html_tag,
                        'vue_type': props.ln_props.vue_type,
                        'page_id': page_id,
                        'websocket_id': websocket_id,
                        'event_data': parent_comp.create_object_from_event(info.event),
                        'old_event_data': parent_comp.create_object_from_event(info.oldEvent),
                        'delta': info.delta,
                        'all_events': parent_comp.get_all_events(calendar)
                    };
                    send_to_server(e, 'event');
                });
            full_calendars[id] = calendar;
            comp_dict[this.$props.ln_props.id] = calendar;

            calendar.render();
        },

    },

    mounted() {
        this.calendar_change();
    },
    updated() {
        var calendar = comp_dict[this.$props.ln_props.id];
        calendar.destroy();
        this.calendar_change();

    },
    props: {
        ln_props: Object
    }
});