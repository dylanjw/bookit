import 'jquery-ui';
import "./../styles/app.scss";
import { attach_calendar, attach_entry_calendar } from "./calendar";
import 'bootstrap';

console.log("Welcome to Bookit!");
attach_calendar('calendar');
attach_entry_calendar('entry_calendar');
