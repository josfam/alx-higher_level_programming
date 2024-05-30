#!/usr/bin/node
/* JQuery:
fetches and lists the title for all movies
by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
Movie titles are listed in the html tag UL#list_movies
*/

const targetItem = $('UL#list_movies');

const insertMovieTitles = function (data) {
  const movies = data.results;
  for (const movie of movies) {
    targetItem.append(`<li>${movie.title}</li>`);
  }
};

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  insertMovieTitles
);
