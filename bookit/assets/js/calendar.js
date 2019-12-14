import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';

export function attach_calendar(elementID) {
    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById(elementID);

        var calendar = new Calendar(calendarEl, {
            plugins: [ dayGridPlugin, listPlugin ],
        });

        calendar.render();
    });
};
