#!/usr/bin/node
/* JQuery:
Adds the class red to the <header> element when the user clicks
on the tag DIV#red_header
*/

const header = $('DIV#red_header');
const addRedClass = function () {
  header.addClass('red');
};
header.on('click', addRedClass);
