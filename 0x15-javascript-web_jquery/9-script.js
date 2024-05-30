#!/usr/bin/node
/* JQuery:
fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the
value of hello from that fetch in the HTML tag DIV#hello
*/

$(document).ready(function () {
  fetchAndInsertTranslation();
});

const targetItem = $('DIV#hello');
const insertTranslation = function (data) {
  targetItem.text(data.hello);
};

const fetchAndInsertTranslation = function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', insertTranslation);
};
