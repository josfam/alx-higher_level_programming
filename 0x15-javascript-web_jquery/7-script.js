#!/usr/bin/node
/* JQuery:
fetches the character `name` from this URL:
https://swapi-api.alx-tools.com/api/people/5/?format=json
*/

const targetItem = $('DIV#character');

const insertName = function (data) {
  const characterName = data.name;
  targetItem.text(characterName);
};

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  insertName
);
