import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';
import interactionPlugin from '@fullcalendar/interaction';

export function attach_entry_calendar(elementID) {
    document.addEventListener('DOMContentLoaded', function() {
    var entryCalendarEl = document.getElementById(elementID);

    let entry_calendar = new Calendar(entryCalendarEl, {
        plugins: [
            dayGridPlugin,
            interactionPlugin
        ],
        selectable: true,
        defaultView: 'dayGridMonth',
        dateClick: function(info) {
            $('a[href="#v-pills-create_form"]').tab('show');
            $('#id_start_0').val(info.startStr)
            $('#id_start_1').val('10am')
            $('#id_end_0').val(info.endStr)
            $('#id_end_1').val('10pm')
            console.log(info)
        },
        select: function(info) {
            $('a[href="#v-pills-create_form"]').tab('show');
            $('#id_start').val(info.startStr)
            $('#id_end').val(info.endStr)
            console.log(info)
        },
    });
    entry_calendar.render()

    // play nice with bootstrap tabs
    var day_grid = entry_calendar.el.getElementsByClassName('fc-day-grid-container')[0]
    day_grid.style.overflow = "visible"
})};


export function attach_calendar(elementID) {
    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById(elementID);

        var calendar = new Calendar(calendarEl, {
            plugins: [ dayGridPlugin, listPlugin ],
            defaultView: 'listMonth',
            events: [
                {
                    title: 'BLF Kitchen Rental',
                    start: '2019-12-18T09:00:00',
                    end: '2019-12-18T15:00:00',
                    extendedProps: {
                        status: 'confirmed',
                    },
                },
                {
                    title: 'BLF Kitchen Rental',
                    start: '2019-12-20T15:00:00',
                    end: '2019-12-20T18:00:00',
                    extendedProps: {
                        status: 'unconfirmed',
                    },
                }
            ],
            eventRender: function(info) {
                if (info.event.extendedProps.status === 'unconfirmed') {

                    var titleTextEl = info.el.getElementsByClassName('fc-list-item-title')[0];
                    if (titleTextEl) {
                        titleTextEl.innerHTML += '<p><em><small>Unconfirmed<small></em></p>'
                    }
                    // Change background color of row
                    info.el.style.backgroundColor = '#dfd1d1';

                    // Change color of dot marker
                    var dotEl = info.el.getElementsByClassName('fc-event-dot')[0];
                    if (dotEl) {
                        dotEl.style.backgroundColor = '#a86c6c';
                    }
                };
                if (info.event.extendedProps.status === 'confirmed') {

                    var titleTextEl = info.el.getElementsByClassName('fc-list-item-title')[0];
                    if (titleTextEl) {
                        titleTextEl.innerHTML += '<p><em><small>Confirmed<small></em></p>'
                    }
                }
            },
        });
        calendar.render();
    });
    

};
