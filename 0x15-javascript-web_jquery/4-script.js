#!/usr/bin/node
/* JQuery:
Toggles the class of the <header> element between red and green,
when the user clicks on the tag DIV#toggle_header
*/

const toggleDiv = $('DIV#toggle_header');
const header = $('header');

const toggleGreenBlue = function () {
  if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.addClass('green');
  }
};
toggleDiv.on('click', toggleGreenBlue);
