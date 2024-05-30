#!/usr/bin/node
/* JQuery:
Adds a <li> element to a list when the user clicks on the tag DIV#add_item
*/

const targetList = $('.my_list');
const itemToClick = $('DIV#add_item');

const appendToList = function () {
  targetList.append('<li>Item</li>');
};

itemToClick.on('click', appendToList);
