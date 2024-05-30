#!/usr/bin/node
/* JQuery:
Updates the text of the <header> element to New Header!!!
when the user clicks on DIV#update_header
*/

const targetItem = $('header');
const itemToClick = $('DIV#update_header');
const changeText = function () {
  targetItem.text('New Header!!!');
};

itemToClick.on('click', changeText);
